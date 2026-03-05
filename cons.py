import argparse
import ssl
from kafka import KafkaConsumer


def main():
    # ============================
    # Arguments CLI
    # ============================
    parser = argparse.ArgumentParser(description="Consumer Kafka SASL_SSL (SCRAM) en continu")

    parser.add_argument(
        "--broker",
        type=str,
        default="vps-fb43df0a.vps.ovh.net:9093",
        help="Adresse du broker Kafka (host:port)"
    )
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="Nom du topic Kafka"
    )
    parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="Nom du user Kafka (SASL)"
    )
    parser.add_argument(
        "--group",
        type=str,
        default="python-consumer-group",
        help="Consumer group id"
    )
    parser.add_argument(
        "--from-beginning",
        action="store_true",
        help="Lire depuis le début (earliest) si aucun offset n'existe pour ce groupe"
    )

    args = parser.parse_args()

    BROKER = args.broker
    TOPIC = args.topic
    USERNAME = args.user
    GROUP_ID = args.group

    # Mot de passe FIXE (comme ton producer)
    PASSWORD = "adminpass"

    # ============================
    # SSL Context (comme ton producer)
    # ============================
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # ============================
    # Kafka Consumer (EN CONTINU)
    # ============================
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=[BROKER],
        security_protocol="SASL_SSL",
        ssl_context=context,
        sasl_mechanism="SCRAM-SHA-256",
        sasl_plain_username=USERNAME,
        sasl_plain_password=PASSWORD,
        group_id=GROUP_ID,
        enable_auto_commit=True,
        auto_offset_reset="earliest" if args.from_beginning else "latest",
        value_deserializer=lambda v: v.decode("utf-8", errors="replace"),
        # ⚠️ IMPORTANT : ne pas mettre consumer_timeout_ms => attend indéfiniment
    )

    print(
        f"📥 Consumer démarré (en continu)\n"
        f"   broker={BROKER}\n"
        f"   topic={TOPIC}\n"
        f"   group={GROUP_ID}\n"
        f"   user={USERNAME}\n"
        f"👉 Ctrl+C pour arrêter\n"
    )

    try:
        for msg in consumer:
            print(
                f"➡️ Reçu | topic={msg.topic} partition={msg.partition} "
                f"offset={msg.offset} value='{msg.value}'"
            )
    except KeyboardInterrupt:
        print("\n🛑 Arrêt demandé (Ctrl+C).")
    finally:
        consumer.close()
        print("✅ Consumer fermé.")


if __name__ == "__main__":
    main()

