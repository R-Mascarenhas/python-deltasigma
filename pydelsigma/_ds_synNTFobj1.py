# -*- coding: utf-8 -*-
# _ds_synNTFobj1.py
# Module providing the ds_synNTFobj1 function
# Copyright 2013 Giuseppe Venturini
# This file is part of python-deltasigma.
#
# python-deltasigma is a 1:1 Python replacement of Richard Schreier's 
# MATLAB delta sigma toolbox (aka "delsigma"), upon which it is heavily based.
# The delta sigma toolbox is (c) 2009, Richard Schreier.
#
# python-deltasigma is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for the licensing terms.

"""Module providing the ds_synNTFobj1() function
"""

import numpy as np

from ._padt import padt
from ._padb import padb 
from ._ds_f1f2 import ds_f1f2 
from ._utils import zpk, db, carray
from ._utils import db
from ._rmsGain import rmsGain

def ds_synNTFobj1(x, p, osr, f0):
	"""y = ds_synNTFobj1(x, p, osr, f0)	
	Objective function for synthesizeNTF() 
	"""
	p = carray(p)
	z = np.exp(2j*np.pi*(f0 + 0.5/osr*x))
	z = carray(z)
	if f0 > 0:
		z = padt(z, p.shape[0]/2., np.exp(2j*np.pi*f0))

	z = np.hstack((z, np.conj(z))) 
	z = z[:]
	if f0 == 0:
		z = padb(z, p.shape[0], 1)

	f1, f2 = ds_f1f2(osr, f0)
	ntf = zpk(z, p, 1)
	y = db(rmsGain(ntf, f1, f2))
	return y

def test_ds_synNTFobj1():
	"""Test function for ds_synNTFobj1()
	"""
	ds_synNTFobj1(.5, (.9, 2), 64, .1)
	#FIXME! need proper test function
