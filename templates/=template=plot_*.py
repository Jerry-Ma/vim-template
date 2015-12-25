#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Create Date    :  %FDATE%
# Python Version :  %PYVER%
# Git Repo       :  %GITHUB%
# Email Address  :  %MAIL%
"""
%FFILE%%HERE%
"""

from __future__ import division
import numpy as np

from mympl import SolarizedColor as sc
from mympl import TexStyle as ts
import mympl


if __name__ == '__main__':

    canvas = mympl.CanvasOne(
        width=mympl.emulateapj,
        aspect=0.618,
        scale=1,
        usetw=False,
        )
    fig, (ax, ) = canvas.parts()

    canvas.save_or_show(name,
                        bbox_inches='tight',
                        pad_inches=0,
                        )
