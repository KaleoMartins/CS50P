msg = input("Cumprimente o banco: ").strip().lower()
if msg.startswith("hello"):
    print("$0")
elif msg.startswith("h"):
    print("$20")
else:
    print("$100")