from typing import List
from ifermi.fermi_surface import *

class BandStructure:
    def __init__(self, structure: Structure, slice_type):
        """

        :param structure:
        """

        self._structure = structure
        self._slice_type = slice_type


    def build_band_structure(self, slices: List[FermiSlice]):

        mesh = np.zeros(0)

        for item in slices:
            mesh = np.vstack(mesh, item)


    def get_slices(self, mu_list):

        slices = []

        for mu in mu_list:

            slices.append(FermiSlice(self._slice_type, mu, self._structure))

        return slices