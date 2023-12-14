# main.py

from services.database.db_connection import connect_to_db, close_connection
from services.deck_analysis.deck_processor import analyze_deck, suggest_deck


def main():
    # Conectar ao banco de dados
    conn = connect_to_db()

    # Exemplo de como você pode usar as funções
    # Você vai precisar implementar a lógica real para análise e sugestão de decks
    analyze_deck(...)
    suggest_deck(...)

    # Fechar conexão com o banco de dados
    close_connection(conn)


if __name__ == "__main__":
    main()
