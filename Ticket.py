import json
import os
import uuid

MOVIES_FILE = "movies.json"
BOOKINGS_FILE = "bookings.json"

# -----------------------
# Utility: JSON helpers
# -----------------------
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# -----------------------
# Initial data
# -----------------------
def init_data():
    default_movies = {
        # structure: movie_id -> {title, showtimes: {time_id: {...}}}
    }

    # Create two movies with two showtimes each for demo
    default_movies = {
        "m1": {
            "title": "The Adventure Begins",
            "showtimes": {
                "s1": {"time": "10:00 AM", "rows": 5, "cols": 8, "price": 150.0, "seats": []},
                "s2": {"time": "06:30 PM", "rows": 6, "cols": 9, "price": 200.0, "seats": []},
            },
        },
        "m2": {
            "title": "Romance in Pythonia",
            "showtimes": {
                "s3": {"time": "01:00 PM", "rows": 5, "cols": 8, "price": 120.0, "seats": []},
                "s4": {"time": "09:00 PM", "rows": 6, "cols": 9, "price": 220.0, "seats": []},
            },
        },
    }

    # Initialize seat maps if empty
    for m in default_movies.values():
        for s in m["showtimes"].values():
            if not s.get("seats"):
                r = s["rows"]
                c = s["cols"]
                # False = available, True = booked
                s["seats"] = [[False for _ in range(c)] for _ in range(r)]

    movies = load_json(MOVIES_FILE, default_movies)
    bookings = load_json(BOOKINGS_FILE, {})

    # In case movies.json exists but seats missing (backwards compat), ensure seats present
    for m in movies.values():
        for s in m["showtimes"].values():
            if "seats" not in s or not s["seats"]:
                r = s["rows"]
                c = s["cols"]
                s["seats"] = [[False for _ in range(c)] for _ in range(r)]

    save_json(MOVIES_FILE, movies)
    save_json(BOOKINGS_FILE, bookings)
    return movies, bookings

# -----------------------
# Helpers for seat display
# -----------------------
def display_seat_map(seats):
    # seats: list of lists of booleans
    rows = len(seats)
    cols = len(seats[0]) if rows else 0
    header = "   " + " ".join(f"{i+1:2}" for i in range(cols))
    print(header)
    for r in range(rows):
        row_label = chr(ord("A") + r)
        row_str = f"{row_label}  "
        for c in range(cols):
            row_str += " X" if seats[r][c] else " O"
        print(row_str)
    print("O = available, X = booked")

def seat_to_index(seat_str):
    # seat_str e.g., "A3" -> (row_index, col_index)
    seat_str = seat_str.strip().upper()
    if len(seat_str) < 2:
        return None
    row_char = seat_str[0]
    col_part = seat_str[1:]
    if not row_char.isalpha() or not col_part.isdigit():
        return None
    row = ord(row_char) - ord("A")
    col = int(col_part) - 1
    return row, col

def index_to_seat(r, c):
    return f"{chr(ord('A') + r)}{c+1}"

# -----------------------
# Booking operations
# -----------------------
def list_movies(movies):
    print("\nAvailable Movies & Showtimes:")
    for mid, m in movies.items():
        print(f"{mid}: {m['title']}")
        for sid, s in m["showtimes"].items():
            available = sum(1 for row in s["seats"] for seat in row if not seat)
            total = s["rows"] * s["cols"]
            print(f"   {sid} - {s['time']}  | Price: ₹{s['price']:.2f} | Available: {available}/{total}")
    print()

def choose_movie_show(movies):
    list_movies(movies)
    mid = input("Enter movie id (e.g. m1): ").strip()
    if mid not in movies:
        print("Invalid movie id.")
        return None, None
    movie = movies[mid]
    sid = input("Enter showtime id (e.g. s1): ").strip()
    if sid not in movie["showtimes"]:
        print("Invalid showtime id.")
        return None, None
    return mid, sid

def book_tickets(movies, bookings):
    mid, sid = choose_movie_show(movies)
    if not mid:
        return
    m = movies[mid]
    s = m["showtimes"][sid]
    print(f"\nYou selected: {m['title']} at {s['time']} (Price per seat: ₹{s['price']:.2f})")
    display_seat_map(s["seats"])

    seat_input = input("Enter seats to book separated by commas (e.g. A1,A2): ").strip()
    desired = [x.strip() for x in seat_input.split(",") if x.strip()]
    indices = []
    for seat in desired:
        idx = seat_to_index(seat)
        if idx is None:
            print(f"Ignoring invalid seat format: {seat}")
            continue
        r, c = idx
        if r < 0 or r >= s["rows"] or c < 0 or c >= s["cols"]:
            print(f"Seat out of range: {seat}")
            continue
        if s["seats"][r][c]:
            print(f"Seat already booked: {seat}")
            continue
        indices.append((r, c))

    if not indices:
        print("No valid seats chosen.")
        return

    total_price = len(indices) * s["price"]
    print(f"Seats to book: {', '.join(index_to_seat(r,c) for r,c in indices)}")
    print(f"Total price: ₹{total_price:.2f}")

    confirm = input("Confirm booking? (y/n): ").strip().lower()
    if confirm != "y":
        print("Booking cancelled.")
        return

    # Mock payment step
    print("Processing payment... (mock)")
    # Mark seats as booked
    for r, c in indices:
        s["seats"][r][c] = True

    # Create booking record
    booking_id = str(uuid.uuid4())[:8]
    booking = {
        "id": booking_id,
        "movie_id": mid,
        "movie_title": m["title"],
        "show_id": sid,
        "time": s["time"],
        "seats": [index_to_seat(r, c) for r, c in indices],
        "price_per_seat": s["price"],
        "total": total_price,
    }
    bookings[booking_id] = booking
    save_json(MOVIES_FILE, movies)
    save_json(BOOKINGS_FILE, bookings)
    print(f"Booking confirmed! Your booking ID: {booking_id}")
    print("Enjoy the movie! 🎬")

def view_bookings(bookings):
    if not bookings:
        print("No bookings yet.")
        return
    print("\nYour Bookings:")
    for bid, b in bookings.items():
        print(f"ID: {bid} | {b['movie_title']} at {b['time']} | Seats: {', '.join(b['seats'])} | Total: ₹{b['total']:.2f}")

def cancel_booking(movies, bookings):
    view_bookings(bookings)
    bid = input("Enter booking ID to cancel: ").strip()
    if bid not in bookings:
        print("Invalid booking ID.")
        return
    b = bookings[bid]
    # Unlock seats in movies data
    m = movies[b["movie_id"]]
    s = m["showtimes"][b["show_id"]]
    for seat in b["seats"]:
        idx = seat_to_index(seat)
        if idx:
            r, c = idx
            if 0 <= r < s["rows"] and 0 <= c < s["cols"]:
                s["seats"][r][c] = False
    # Remove booking
    del bookings[bid]
    save_json(MOVIES_FILE, movies)
    save_json(BOOKINGS_FILE, bookings)
    print(f"Booking {bid} cancelled and seats released.")

# -----------------------
#  ################Main menu # #####################

def main():
    movies, bookings = init_data()
    print("=== Welcome to Simple Movie Booking ===")

    while True:
        print("\nMenu:")
        print("1. List movies & showtimes")
        print("2. Book tickets")
        print("3. View my bookings")
        print("4. Cancel a booking")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            list_movies(movies)
        elif choice == "2":
            book_tickets(movies, bookings)
        elif choice == "3":
            view_bookings(bookings)
        elif choice == "4":
            cancel_booking(movies, bookings)
        elif choice == "5":
            print("Thanks for using the Movie Booking demo. Bye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
