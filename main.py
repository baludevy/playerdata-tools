import argparse
import uuid, hashlib
import os


# Generates an Offline Minecraft Name UUID
def generate_name_uuid(name: str) -> uuid.UUID:
    """
    Generates an Offline Minecraft Name UUID
    """
    # name to bytes
    name_bytes = f"OfflinePlayer:{name}".encode("utf-8")

    # md5 hashing
    hash = hashlib.md5(name_bytes).digest()

    return uuid.UUID(bytes=hash[:16], version=3)


def file_format(uuid: str) -> str:
    """
    Returns a string with the .dat fileformat ending
    """
    return f"{uuid}.dat"


# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument("operation", type=str, help="Operation to perform (swap, move)")
parser.add_argument("source_player", type=str, help="Original player name, username1")
parser.add_argument("target_player", type=str, help="New player name, username2")

args = parser.parse_args()
source_player_name = args.source_player
target_player_name = args.target_player

# Generate name uuid and format them to .dat filenames
source_player_data = file_format(generate_name_uuid(source_player_name))
target_player_data = file_format(generate_name_uuid(target_player_name))


def swap() -> None:
    """
    Swaps two player's playerdata
    """
    if os.path.exists(source_player_data) is not True:
        print(
            f"Source playerdata doesn't exist! Username: {source_player_name}; UUID: {generate_name_uuid(source_player_name)}"
        )
        return
    if os.path.exists(target_player_data) is not True:
        print(
            f"Target playerdata doesn't exist! Username: {target_player_name}; UUID: {generate_name_uuid(target_player_name)}"
        )
        return
    # Rename the two files temporarily so that their names dont collide when swapping the two filenames
    os.rename(source_player_data, f"{source_player_data}.tmp")
    os.rename(target_player_data, f"{target_player_data}.tmp")

    # Rename the temporary files to swap the two player's playerdata
    os.rename(f"{source_player_data}.tmp", target_player_data)
    os.rename(f"{target_player_data}.tmp", source_player_data)


def move() -> None:
    """
    Moves a player's playerdata to another username
    """
    if os.path.exists(source_player_data) is not True:
        print(
            f"Source playerdata doesn't exist! Username: {args.source_player}; UUID: {generate_name_uuid(source_player_name)}"
        )
        return
    os.rename(source_player_data, f"{target_player_data}")


def main() -> None:
    if args.operation == "swap":
        swap()
    if args.operation == "move":
        move()


if __name__ == "__main__":
    main()
