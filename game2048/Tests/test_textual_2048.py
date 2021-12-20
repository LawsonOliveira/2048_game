from pytest import *
from io import StringIO
from game2048.textual_2048 import read_player_command

def test_read_player_command(monkeypatch):
    
    #Test la fonction read_player_command en utilisant un mock
    
    command_h = StringIO('h\n')
    monkeypatch.setattr('sys.stdin',command_h)
    assert read_player_command() == 'h'

    command_g = StringIO('g\n')
    monkeypatch.setattr('sys.stdin',command_g)
    assert read_player_command() == 'g'

    command_d = StringIO('d\n')
    monkeypatch.setattr('sys.stdin',command_d)
    assert read_player_command() == 'd'

    command_b = StringIO('b\n')
    monkeypatch.setattr('sys.stdin',command_b)
    assert read_player_command() == 'b'

test_read_player_command(MonkeyPatch())
