import pytest
import json

from randovania.layout.layout_description import LayoutDescription
from randovania.games.super_metroid.patcher.super_duper_metroid_patcher import SuperDuperMetroidPatcher
from randovania.interface_common.players_configuration import PlayersConfiguration
from randovania.games.super_metroid.layout.super_metroid_cosmetic_patches import SuperMetroidCosmeticPatches

def test_patch_data_creation(test_files_dir):
    # Load the RDV game
    game_file = test_files_dir.joinpath("sdm_test_game.rdvgame").open()
    game_json = json.load(game_file)
    game_file.close()
    layout = LayoutDescription.from_json_dict(game_json)

    # Create patch_data from layout
    patcher = SuperDuperMetroidPatcher()
    player_configuration = PlayersConfiguration(0, {0: "Player"})
    cosmetic_patches = SuperMetroidCosmeticPatches()

    patch_data = patcher.create_patch_data(layout, player_configuration, cosmetic_patches)

    # Load control patch_data and compare the two for differences
    json_file = test_files_dir.joinpath("sdm_expected_result.json").open()
    expected_json = json.load(json_file)
    json_file.close()
    assert expected_json == patch_data


