import argparse
import mc_uuid_utils
import file_utils

parser = argparse.ArgumentParser()

parser.add_argument("operation", type=str, help="Operation to perform (swap, move)")
parser.add_argument("source_player", type=str, help="Original player name")
parser.add_argument("target_player", type=str, help="New player name")

args = parser.parse_args()
source_player_name = args.source_player
target_player_name = args.target_player

source_player_data = mc_uuid_utils.file_format(
    mc_uuid_utils.generate_name_uuid(source_player_name)
)
target_player_data = mc_uuid_utils.file_format(
    mc_uuid_utils.generate_name_uuid(target_player_name)
)


def swap():
    file_utils.rename_file(source_player_data, f"{source_player_data}.tmp")
    file_utils.rename_file(target_player_data, f"{target_player_data}.tmp")

    file_utils.rename_file(f"{source_player_data}.tmp", target_player_data)
    file_utils.rename_file(f"{target_player_data}.tmp", source_player_data)


def main():
    if args.operation == "swap":
        swap()


if __name__ == "__main__":
    main()
