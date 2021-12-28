##############################################################################
#
#    GNU Condo: The Free Management Condominium System
#    Copyright (C) 2016- M. Alonso <port02.server@gmail.com>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from trytond.pool import PoolMeta

__all__ = ['CondoFactors', 'CondoParty', 'Factor', 'Unit']


class CondoFactors(metaclass=PoolMeta):
    __name__ = 'condo.factor'

    @classmethod
    def __setup__(cls):
        super(CondoFactors, cls).__setup__()
        cls._history = True


class CondoParty(metaclass=PoolMeta):
    __name__ = 'condo.party'

    @classmethod
    def __setup__(cls):
        super(CondoParty, cls).__setup__()
        cls._history = True


class Unit(metaclass=PoolMeta):
    __name__ = 'condo.unit'

    @classmethod
    def __setup__(cls):
        super(Unit, cls).__setup__()
        cls._history = True


class Factor(metaclass=PoolMeta):
    __name__ = 'condo.unit-factor'

    @classmethod
    def __setup__(cls):
        super(Factor, cls).__setup__()
        cls._history = True
