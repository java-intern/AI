def vacuum(loc, status):
    if status == 'Dirty':
        print(f"Cleaning {loc}")
    else:
        print(f"{loc} already clean")
    next_loc = 'B' if loc == 'A' else 'A'
    vacuum(next_loc, 'Dirty' if next_loc == 'B' else 'Clean') if loc == 'A' else None

vacuum('A', 'Dirty')
