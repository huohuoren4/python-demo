#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

from abc import abstractmethod, ABC


class Player:
    def __init__(self, face: str, body: str):
        self.face = face
        self.body = body
    def __str__(self):
        return "%s, %s" % (self.face, self.body)


class PlayerBuilder(ABC):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass


class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

class PlayerDirector:
    """
    指挥者: 控制组装顺序
    """

    def build_player(self, builder_obj):
        builder.build_body()
        builder.build_face()
        return builder.player


if __name__ == '__main__':
    builder = Monster()
    director = PlayerDirector()
    p = director.build_player(builder)
