def move_tower(height, from_tower, to_tower, with_tower):
    if height >= 1:
        move_tower(height-1, from_tower, with_tower, to_tower)
        move_disk(height, from_tower, to_tower)
        move_tower(height-1, with_tower, to_tower, from_tower)

def move_disk(num, ft,tt):
    print(f"Moving disk {num} from:{ft}, to:{tt}")

if __name__ == "__main__":
    move_tower(3, 'A', 'C', 'B')