import pandas as pd

# Load CSV file
df = pd.read_csv("books.csv")

# Function to display full report
def display_all_books():
    print("\n📚 Complete Book List:\n")
    print(df.to_string(index=False))


# Function to filter books by author
def books_by_author(author_name):
    result = df[df['Author'].str.lower() == author_name.lower()]
    print(f"\n📖 Books by {author_name}:\n")
    print(result.to_string(index=False))


# Function to filter books by publisher
def books_by_publisher(publisher_name):
    result = df[df['Publisher'].str.lower() == publisher_name.lower()]
    print(f"\n🏢 Books by Publisher: {publisher_name}\n")
    print(result.to_string(index=False))


# Function to find cheapest and costliest books
def price_extremes():
    cheapest = df.loc[df['Price'].idxmin()]
    costliest = df.loc[df['Price'].idxmax()]

    print("\n💰 Cheapest Book:\n", cheapest)
    print("\n💎 Costliest Book:\n", costliest)


# Function to sort by year
def sort_by_year():
    sorted_df = df.sort_values(by='Year')
    print("\n📅 Books Sorted by Publication Year:\n")
    print(sorted_df.to_string(index=False))


# ----------- MENU -----------
while True:
    print("\n===== BOOK MANAGEMENT SYSTEM =====")
    print("1. Display all books")
    print("2. Search books by author")
    print("3. Search books by publisher")
    print("4. Show cheapest and costliest book")
    print("5. Sort books by year")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_all_books()

    elif choice == '2':
        author = input("Enter author name: ")
        books_by_author(author)

    elif choice == '3':
        publisher = input("Enter publisher name: ")
        books_by_publisher(publisher)

    elif choice == '4':
        price_extremes()

    elif choice == '5':
        sort_by_year()

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("❌ Invalid choice. Try again.")
