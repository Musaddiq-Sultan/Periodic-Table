import tkinter as tk

root = tk.Tk()
root.title("Periodic Table")
root.geometry("823x580")
root.resizable(0, 0)

# Creating Frames

frame01 = tk.Frame(root)
frame01.pack(padx=5, pady=5, fill="x")

key_frame = tk.LabelFrame(root, text="Key", font=("Halvetica", 8))
key_frame.pack(padx=5, pady=(0, 5), fill="x")

frame02 = tk.LabelFrame(root, text="Results")
frame02.pack(padx=5, pady=(0, 5), expand=True, fill="both")

# Creating Functions


def clear():
    global frame02
    frame02.destroy()
    frame02 = tk.LabelFrame(root, text="Results")
    frame02.pack(padx=5, pady=(0, 5), expand=True, fill="both")


def H_function():
    clear()
    tk.Message(frame02,
               text='''Name: Hydrogen
Symbol: H
Atomic mass: 1.00784 u
Atomic number: 1
Electronegativity: 2.2
Electron configuration: 1s1
Density (at STP): 0.08988 g/L
Named by: Antoine Lavoisier (1783)''').pack(anchor="w")


def He_function():
    clear()
    tk.Message(frame02,
               text='''Name: Helium
Symbol: He
Atomic number: 2
Atomic mass: 4.002602 u
Electrons per shell: 2
Electron configuration: 1s2
Discovery: Pierre Janssen, Norman Lockyer (1868)
Natural occurrence: primordial''').pack(anchor="w")


def Li_function():
    clear()
    tk.Message(frame02,
               text='''Name: Lithium
Symbol: Li
Atomic number: 3
Atomic mass: 6.941 u
Electrons per shell: 2,1
Electron configuration: [He] 2s1
Natural occurrence: primordial
Crystal structure: ​body-centered cubic (bcc)''').pack(anchor="w")


def Be_function():
    clear()
    tk.Message(frame02,
               text='''Name: Beryllium
Symbol: Be
Atomic number: 4
Atomic mass: 9.012182 u
Electrons per shell: 2,2
Electron configuration: [He] 2s²
Electronegativity: 1.57
Crystal structure: ​hexagonal close-packed (hcp)''').pack(anchor="w")


def B_function():
    clear()
    tk.Message(frame02,
               text='''Name: Boron
Symbol: B
Atomic number: 5
Atomic mass: 10.811 u
Electron configuration: [He] 2s22p1
Electrons per shell: 2,3
Electronegativity: 2.04
Period: Period 2 element''').pack(anchor="w")


def C_function():
    clear()
    tk.Message(frame02,
               text='''Name: Carbon
Atomic number: 6
Symbol: C
Recognized as an element by: Antoine Lavoisier (1789)
Sublimation point: 3915 K ​(3642 °C, ​6588 °F)
Natural occurrence: primordial
Triple point: 4600 K, ​10,800 kPa
Period: period 2
Discovery: Egyptians and Sumerians (3750 BCE)''').pack(anchor="w")


def N_function():
    clear()
    tk.Message(frame02,
               text='''Name: Nitrogen
Symbol: N
Atomic mass: 14.0067 u
Atomic number: 7
Electron configuration: [He] 2s22p3
Density (at STP): 1.2506 g/L at 0 °C, 1013 mbar
Triple point: 63.151 K, ​12.52 kPa
Named by: Jean-Antoine Chaptal (1790)''').pack(anchor="w")


def O_function():
    clear()
    tk.Message(frame02,
               text='''Name: Oxygen
Symbol: O
Atomic mass: 15.999 u
Atomic number: 8
Electron configuration: [He] 2s²2p⁴
Electronegativity: 3.44
Electrons per shell: 2, 6
Discoverers: Joseph Priestley, Antoine Lavoisier, Carl Wilhelm Scheele'''
               ).pack(anchor="w")


def F_function():
    clear()
    tk.Message(frame02,
               text='''Name: Fluorine
Symbol: F
Atomic number: 9
Atomic mass: 18.998403 u
Electronegativity: 3.98
Electron configuration: [He] 2s22p5
Melting point: -219.6 °C
Van der Waals radius: 147 pm''').pack(anchor="w")


def Ne_function():
    clear()
    tk.Message(frame02,
               text='''Name: Neon
Symbol: Ne
Atomic number: 10
Atomic mass: 20.1797 u
Electrons per shell: 2,8
When liquid (at b.p.): 1.207 g/cm3
Period: period 2
Oxidation states: 0''').pack(anchor="w")


def Na_function():
    clear()
    tk.Message(frame02,
               text='''Name: Sodium
Symbol: Na
Atomic mass: 22.989769 u
Electron configuration: [Ne] 3s¹
Atomic number: 11
Atomic radius: empirical: 186 pm
When liquid (at m.p.): 0.927 g/cm3
Crystal structure: ​body-centered cubic (bcc)''').pack(anchor="w")


def Mg_function():
    clear()
    tk.Message(frame02,
               text='''Name: Magnesium
Symbol: Mg
Atomic number: 12
Atomic mass: 24.305 u
Electron configuration: [Ne] 3s2
Oxidation number: 2
Crystal structure: ​hexagonal close-packed (hcp)
Discoverers: Humphry Davy, Joseph Black''').pack(anchor="w")


def Al_function():
    clear()
    tk.Message(frame02,
               text='''Name: Aluminum
Symbol: Al
Atomic number: 13
Atomic mass: 26.981539 u
Electron configuration: [Ne] 3s²3p¹
Electronegativity: 1.61
Crystal structure: ​face-centered cubic (fcc)
Density (near r.t.): 2.70 g/cm3''').pack(anchor="w")


def Si_function():
    clear()
    tk.Message(frame02,
               text='''Name: Silicon
Symbol: Si
Atomic number: 14
Atomic mass: 28.0855 u
Electron configuration: [Ne] 3s²3p²
Melting point: 1,414 °C
Electrons per shell: 2, 8, 4
Crystal structure: ​face-centered diamond-cubic''').pack(anchor="w")


def P_function():
    clear()
    tk.Message(frame02,
               text='''Name: Phosphorus
Symbol: P
Atomic mass: 30.973762 u
Atomic number: 15
Electron configuration: [Ne] 3s²3p³
Electrons per shell: 2, 8, 5
Electronegativity: 2.19
Recognised as an element by: Antoine Lavoisier (1777''').pack(anchor="w")


def S_function():
    clear()
    tk.Message(frame02,
               text='''Name: Sulfur
Symbol: S
Atomic mass: 32.065 u
Atomic number: 16
Electron configuration: [Ne] 3s²3p⁴
Recognized as an element by: Antoine Lavoisier (1777)
Natural occurrence: primordial
Group: Chalcogen (group 16)''').pack(anchor="w")


def Cl_function():
    clear()
    tk.Message(frame02,
               text='''Name: Chlorine
Symbol: Cl
Atomic mass: 35.453 u
Atomic number: 17
Electron configuration: [Ne] 3s²3p⁵
Recognized as an element by: Humphry Davy (1808)
When liquid (at b.p.): 1.5625 g/cm3''').pack(anchor="w")


def Ar_function():
    clear()
    tk.Message(frame02,
               text='''Name: Argon
Symbol: Ar
Atomic mass: 39.948 u
Electron configuration: [Ne] 3s²3p⁶
Atomic number: 18
When liquid (at b.p.): 1.3954 g/cm3
Density (at STP): 1.784 g/L''').pack(anchor="w")


def K_function():
    clear()
    tk.Message(frame02,
               text='''Name: Potassium
Symbol: K
Atomic mass: 39.0983 u
Atomic number: 19
Electron configuration: [Ar] 4s¹
Van der Waals radius: 280 pm
Boiling point: 758.8 °C''').pack(anchor="w")


def Ca_function():
    clear()
    tk.Message(frame02,
               text='''Name: Calcium
Symbol: Ca
Atomic number: 20
Atomic mass: 40.078 u
Electron configuration: [Ar] 4s²
Atomic radius: empirical: 197 pm
Period: period 4
Crystal structure: ​face-centred cubic (fcc)''').pack(anchor="w")


def Sc_function():
    clear()
    tk.Message(frame02,
               text='''Name: Scandium
Symbol: Sc
Atomic number: 21
Atomic radius: empirical: 162 pm
Oxidation states: 0, +1, +2, +3 (an amphoteric oxide)
Period: period 4
Group: group 3
Naming: after Scandinavia''').pack(anchor="w")


def Ti_function():
    clear()
    tk.Message(frame02,
               text='''Name: Titanium
Symbol: Ti
Atomic number: 22
Atomic mass: 47.867 u
Electron configuration: [Ar] 3d24s2
Electrons per shell: 2, 8, 10, 2
Oxidation states: −2, −1, 0, +1, +2, +3, +4 (an amphoteric oxide)
Named by: Martin Heinrich Klaproth (1795)''').pack(anchor="w")


def V_function():
    clear()
    tk.Message(frame02,
               text='''Name: Vanadium
Atomic number: 23
Symbol: V
Oxidation states: −3, −1, 0, +1, +2, +3, +4, +5 (an amphoteric oxide)
Period: period 4
Atomic radius: empirical: 134 pm
Named by: Nils Gabriel Sefström (1830)
Crystal structure: ​body-centered cubic (bcc)
Natural occurrence: primordial''').pack(anchor="w")


def Cr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Chromium
Symbol: Cr
Atomic number: 24
Atomic mass: 51.9961 u
Electron configuration: [Ar] 3d⁵4s¹
Melting point: 1,907 °C
Van der Waals radius: 200 pm
Boiling point: 2,672 °C''').pack(anchor="w")


def Mn_function():
    clear()
    tk.Message(frame02,
               text='''Name: Manganese
Symbol: Mn
Atomic number: 25
Crystal structure: ​body-centered cubic (bcc)
Magnetic ordering: paramagnetic
Atomic radius: empirical: 127 pm
Magnetic susceptibility: (α) +529.0·10−6 cm3/mol (293 K)
Natural occurrence: primordial''').pack(anchor="w")


def Fe_function():
    clear()
    tk.Message(frame02,
               text='''Name: Iron
Symbol: Fe
Atomic mass: 55.845 u
Atomic number: 26
Melting point: 1,538 °C
Electron configuration: [Ar] 3d64s2
Density: 7.874 g/cm³ (near room temperature)
Natural occurrence: primordial''').pack(anchor="w")


def Co_function():
    clear()
    tk.Message(frame02,
               text='''Name: Cobalt
Symbol: Co
Atomic number: 27
Atomic mass: 58.933195 u
Oxidation states: −3, −1, 0, +1, +2, +3, +4, +5 (an amphoteric oxide)
Natural occurrence: primordial
Atomic radius: empirical: 125 pm
Crystal structure: ​hexagonal close-packed (hcp)''').pack(anchor="w")


def Ni_function():
    clear()
    tk.Message(frame02,
               text='''Name: Nickel
Symbol: Ni
Atomic mass: 58.6934 u
Atomic number: 28
Electron configuration: [Ar] 3d⁸4s²
Oxidation states: −2, −1, 0, +1, +2, +3, +4 (a mildly basic oxide)
Crystal structure: ​face-centered cubic (fcc)
Atomic radius: empirical: 124 pm''').pack(anchor="w")


def Cu_function():
    clear()
    tk.Message(frame02,
               text='''Name: Copper
Symbol: Cu
Atomic mass: 63.546 u
Atomic number: 29
Electron configuration: [Ar] 3d¹⁰4s¹
Melting point: 1,085 °C
Density: 8.96 g/cm³ (Near room temperature)
Crystal structure: ​face-centered cubic (fcc)''').pack(anchor="w")


def Zn_function():
    clear()
    tk.Message(frame02,
               text='''Name: Zinc
Symbol: Zn
Atomic mass: 65.38 u
Atomic number: 30
Electron configuration: [Ar] 3d¹⁰4s²
Recognized as a unique metal by: Rasaratna Samuccaya (1300)
Oxidation states: −2, 0, +1, +2 (an amphoteric oxide)
Crystal structure: ​hexagonal close-packed (hcp)''').pack(anchor="w")


def Ga_function():
    clear()
    tk.Message(frame02,
               text='''Name: Gallium
Symbol: Ga
Atomic number: 31
Atomic mass: 69.723 u
Electron configuration: [Ar] 3d104s24p1
When liquid (at m.p.): 6.095 g/cm3
Atomic radius: empirical: 135 pm
Crystal structure: ​orthorhombic''').pack(anchor="w")


def Ge_function():
    clear()
    tk.Message(frame02,
               text='''Name: Germanium
Symbol: Ge
Atomic number: 32
Electron configuration: [Ar] 3d¹⁰4s²4p²
Atomic mass: 72.64 u
Atomic radius: empirical: 122 pm
Crystal structure: ​face-centered diamond-cubic
Electrons per shell: 2, 8, 18, 4''').pack(anchor="w")


def As_function():
    clear()
    tk.Message(frame02,
               text='''Name: Arsenic
Symbol: As
Atomic number: 33
Atomic radius: empirical: 119 pm
Crystal structure: ​rhombohedral
Oxidation states: −3, −2, −1, 0, +1, +2, +3, +4, +5 (a mildly acidic oxide)
Natural occurrence: primordial
Period: period 4''').pack(anchor="w")


def Se_function():
    clear()
    tk.Message(frame02,
               text='''Name: Selenium
Symbol: Se
Atomic number: 34
Atomic mass: 78.96 u
Electrons per shell: 2,8,18,6
Electron configuration: [Ar] 3d104s24p4
Crystal structure: ​hexagonal
Period: period 4''').pack(anchor="w")


def Br_function():
    clear()
    tk.Message(frame02,
               text='''Name: Bromine
Symbol: Br
Atomic number: 35
Atomic mass: 79.904 u
Electron configuration: [Ar] 4s²3d¹⁰4p⁵
Atomic radius: empirical: 120 pm
Period: period 4
Oxidation states: −1, +1, +3, +4, +5, +7 (a strongly acidic oxide)''').pack(
                   anchor="w")


def Kr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Krypton
Symbol: Kr
Atomic number: 36
Atomic mass: 83.798 u
Electron configuration: [Ar] 3d¹⁰4s²4p⁶
Period: period 4
Crystal structure: ​face-centered cubic (fcc)
Oxidation states: 0, +1, +2 (rarely more than 0; oxide is unknown)''').pack(
                   anchor="w")


def Rb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Rubidium
Symbol: Rb
Atomic number: 37
Electron configuration: [Kr] 5s¹
Atomic mass: 85.4678 u
Period: period 5
Electrons per shell: 2, 8, 18, 8, 1
Crystal structure: ​body-centered cubic (bcc)''').pack(anchor="w")


def Sr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Strontium
Symbol: Sr
Atomic number: 38
Electrons per shell: 2,8,18,8,2
Electron configuration: [Kr] 5s2
Atomic mass: 87.62 u
Period: period 5
Natural occurrence: primordial''').pack(anchor="w")


def Y_function():
    clear()
    tk.Message(frame02,
               text='''Name: Yttrium
Symbol: Y
Atomic number: 39
Electron configuration: [Kr] 4d15s2
Period: period 5
Oxidation states: 0, +1, +2, +3 (a weakly basic oxide)
Naming: after Ytterby (Sweden) and its mineral ytterbite (gadolinite)
Crystal structure: ​hexagonal close-packed (hcp)''').pack(anchor="w")


def Zr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Zirconium
Symbol: Zr
Atomic number: 40
Atomic mass: 91.224 u
Electron configuration: [Kr] 4d²5s²
Oxidation states: −2, 0, +1, +2, +3, +4 (an amphoteric oxide)
Atomic radius: empirical: 160 pm
Crystal structure: ​hexagonal close-packed (hcp)''').pack(anchor="w")


def Nb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Niobium
Symbol: Nb
Atomic mass: 92.90638 u
Electron configuration: [Kr] 4d⁴5s¹
Atomic number: 41
Melting point: 2,477 °C
Van der Waals radius: 207 pm
Discovered: 1801''').pack(anchor="w")


def Mo_function():
    clear()
    tk.Message(frame02,
               text='''Name: Molybdenum
Symbol: Mo
Atomic mass: 95.95 u
Atomic number: 42
Electron configuration: [Kr] 4d₅5s₁
Melting point: 2,623 °C
Discovered: 1778
Electronegativity: 2.16''').pack(anchor="w")


def Tc_function():
    clear()
    tk.Message(frame02,
               text='''Name: Technetium
Symbol: Tc
Atomic mass: 98 u
Atomic number: 43
Electron configuration: [Kr] 4d55s2
Discovered: 1937
Melting point: 2,157 °C
Discoverers: Emilio Segrè, Carlo Perrier''').pack(anchor="w")


def Ru_function():
    clear()
    tk.Message(frame02,
               text='''Name: Ruthenium
Symbol: Ru
Atomic mass: 101.07 u
Electron configuration: [Kr] 4d75s1
Atomic number: 44
Melting point: 2,334 °C
Van der Waals radius: 205 pm
CAS ID: 7440-18-8''').pack(anchor="w")


def Rh_function():
    clear()
    tk.Message(frame02,
               text='''Name: Rhodium
Symbol: Rh
Atomic mass: 102.9055 u
Electron configuration: [Kr] 4d85s1
Atomic number: 45
CAS ID: 7440-16-
Melting point: 1,964 °C
Discovered: 1803''').pack(anchor="w")


def Pd_function():
    clear()
    tk.Message(frame02,
               text='''Name: Palladium
Symbol: Pd
Atomic number: 46
Atomic mass: 106.42 u
Electron configuration: [Kr] 4d¹⁰
Melting point: 1,555 °C
Discovered: 1802
Chemical series: Metal, Transition metal, Toxic heavy metal, Period 5 element, Group 10 element'''
               ).pack(anchor="w")


def Ag_function():
    clear()
    tk.Message(frame02,
               text='''Name: Silver
Symbol: Ag
Atomic mass: 107.8682 u
Atomic number: 47
Electron configuration: [Kr] 4d¹⁰5s¹
Melting point: 961.8 °C
Density: 10.49 g/cm³
Boiling point: 2,162 °C''').pack(anchor="w")


def Cd_function():
    clear()
    tk.Message(frame02,
               text='''Name: Cadmium
Symbol: Cd
Electron configuration: [Kr] 4d¹⁰5s²
Atomic mass: 112.411 u
Atomic number: 48
Melting point: 321.1 °C
Discovered: 1817
CAS ID: 7440-43-9''').pack(anchor="w")


def In_function():
    clear()
    tk.Message(frame02,
               text='''Name: Indium
Symbol: In
Atomic mass: 114.818 u
Atomic number: 49
Electron configuration: [Kr] 4d105s25p1
Melting point: 156.6 °C
Van der Waals radius: 220 pm
Electronegativity: 1.78''').pack(anchor="w")


def Sn_function():
    clear()
    tk.Message(frame02,
               text='''Name: Tin
Symbol: Sn
Electrons per shell: 2, 8, 18, 18, 4
Atomic mass: 118.71 u
Atomic number: 50
Electron configuration: [Kr] 5s²4d¹⁰5p²
Melting point: 231.9 °C
Electronegativity: 1.96''').pack(anchor="w")


def Sb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Antimony
Symbol: Sb
Atomic mass: 121.76 u
Atomic number: 51
Electron configuration: [Kr] 4d105s25p3
Melting point: 630.6 °C
Discovered: 3000 BC
Van der Waals radius: 206 pm''').pack(anchor="w")


def Te_function():
    clear()
    tk.Message(frame02,
               text='''Name: Tellurium
Symbol: Te
Electrons per shell: 2,8,18,18,6
Atomic mass: 127.6 u
Atomic number: 52
Electron configuration: [Kr] 4d105s25p4
Electronegativity: 2.1
Van der Waals radius: 210 pm''').pack(anchor="w")


def I_function():
    clear()
    tk.Message(frame02,
               text='''Name: Iodine
Symbol: I
Atomic mass: 126.90447 u
Atomic number: 53
Electron configuration: [Kr] 4d105s25p5
Electronegativity: 2.66
Melting point: 113.7 °C
Discovered: 1811''').pack(anchor="w")


def Xe_function():
    clear()
    tk.Message(frame02,
               text='''Name: Xenon
Symbol: Xe
Atomic mass: 131.293 u
Electrons per shell: 2,8,18,18,8
Atomic number: 54
Electron configuration: [Kr] 4d¹⁰5s²5p⁶
Boiling point: -108.1 °C
Melting point: -111.8 °C''').pack(anchor="w")


def Cs_function():
    clear()
    tk.Message(frame02,
               text='''Name: Caesium
Symbol: Cs
Atomic mass: 132.90545 u
Atomic number: 55
Electron configuration: [Xe] 6s1
Melting point: 28.44 °C
Van der Waals radius: 343 pm
Electronegativity: 0.79''').pack(anchor="w")


def Ba_function():
    clear()
    tk.Message(frame02,
               text='''Name: Barium
Symbol: Ba
Atomic mass: 137.327 u
Atomic number: 56
Electron configuration: [Xe] 6s2
Van der Waals radius: 268 pm
Electronegativity: 0.89
Melting point: 727 °C''').pack(anchor="w")


def Lu_function():
    clear()
    tk.Message(frame02,
               text='''Name: Lutetium
Symbol: Lu
Electron configuration: [Xe] 4f145d16s2
Atomic number: 71
CAS ID: 7439-94-3
Van der Waals radius: 227 pm
Atomic mass: 174.967 u
Discovered: 1907''').pack(anchor="w")


def Hf_function():
    clear()
    tk.Message(frame02,
               text='''Name: Hafnium
Symbol: Hf
Atomic mass: 178.49 u
Atomic number: 72
Electron configuration: [Xe] 4f¹⁴5d²6s²
Van der Waals radius: 225 pm
Electronegativity: 1.3
Melting point: 2,233 °C''').pack(anchor="w")


def Ta_function():
    clear()
    tk.Message(frame02,
               text='''Name: Tantalum
Symbol: Ta
Atomic mass: 180.94788 u
Atomic number: 73
Electron configuration: [Xe] 4f145d36s2
Melting point: 3,017 °C
Van der Waals radius: 220 pm
Chemical series: Metal, Transition metal, Toxic heavy metal, Group 5 element, Period 6 element'''
               ).pack(anchor="w")


def W_function():
    clear()
    tk.Message(frame02,
               text='''Name: Tungsten
Symbol: W
Atomic mass: 183.84 u
Atomic number: 74
Electron configuration: [Xe] 6s²4f¹⁴5d⁴
Melting point: 3,422 °C
Boiling point: 5,555 °C
Discoverer: Carl Wilhelm Scheele''').pack(anchor="w")


def Re_function():
    clear()
    tk.Message(frame02,
               text='''Name: Rhenium
Symbol: Re
Electrons per shell: 2, 8, 18, 32, 13, 2
Electron configuration: [Xe] 4f145d56s2
Atomic number: 75
Atomic mass: 186.207 u
Melting point: 3,185 °C
Discoverers: Ida Noddack, Walter Noddack, Otto Berg''').pack(anchor="w")


def Os_function():
    clear()
    tk.Message(frame02,
               text='''Name: Osmium
Symbol: Os
Atomic mass: 190.23 u
Atomic number: 76
Electron configuration: [Xe] 4f145d66s2
Melting point: 3,033 °C
CAS ID: 7440-04-2
Chemical series: Metal, Transition metal, Toxic heavy metal, Period 6 element, Group 8 element'''
               ).pack(anchor="w")


def Ir_function():
    clear()
    tk.Message(frame02,
               text='''Name: Iridium
Symbol: Ir
Atomic mass: 192.217 u
Electron configuration: [Xe] 4f145d76s2
Atomic number: 77
Melting point: 2,466 °C
Van der Waals radius: 200 pm
Discoverer: Smithson Tennant''').pack(anchor="w")


def Pt_function():
    clear()
    tk.Message(frame02,
               text='''Name: Platinum
Symbol: Pt
Atomic mass: 195.084 u
Atomic number: 78
Electron configuration: [Xe] 4f145d96s1
Melting point: 1,768 °C
Boiling point: 3,825 °C
Discoverer: Antonio de Ulloa''').pack(anchor="w")


def Au_function():
    clear()
    tk.Message(frame02,
               text='''Name: Gold
Symbol: Au
Electron configuration: [Xe] 4f145d106s1
Melting point: 1,064 °C
Atomic number: 79
Atomic mass: 196.96657 u
Boiling point: 2,700 °C
Symbol of: California, Alaska''').pack(anchor="w")


def Hg_function():
    clear()
    tk.Message(frame02,
               text='''Name: Mercury
Symbol: Hg
Electrons per shell: 2,8,18,32,18,2
Atomic mass: 200.59 u
Atomic number: 80
Boiling point: 356.7 °C
Melting point: -38.83 °C
Electron configuration: [Xe] 4f145d106s2''').pack(anchor="w")


def Tl_function():
    clear()
    tk.Message(frame02,
               text='''Name: Thallium
Symbol: Tl
Atomic mass: 204.3833 u
Atomic number: 81
Electron configuration: [Xe] 4f145d106s26p1
Melting point: 304 °C
Electronegativity: 1.62
Van der Waals radius: 220 pm''').pack(anchor="w")


def Pb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Lead
Symbol: Pb
Atomic mass: 207.2 u
Atomic number: 82
Melting point: 327.5 °C
Electron configuration: [Xe] 6s²4f¹⁴5d¹⁰6p²
Electrons per shell: 2,8,18,32,18,4
Boiling point: 1,749 °C''').pack(anchor="w")


def Bi_function():
    clear()
    tk.Message(frame02,
               text='''Name: Bismuth
Symbol: Bi
Atomic mass: 208.9804 u
Atomic number: 83
Electron configuration: [Xe] 4f145d106s26p3
Melting point: 271.4 °C
Van der Waals radius: 230 pm
Discoverer: Claude François Geoffroy''').pack(anchor="w")


def Po_function():
    clear()
    tk.Message(frame02,
               text='''Name: Polonium
Symbol: Po
Atomic mass: 209 u
Electrons per shell: 2,8,18,32,18,6
Atomic number: 84
Electron configuration: [Xe] 6s24f145d106p4
Discovered: 1898
Discoverers: Marie Curie, Pierre Curie''').pack(anchor="w")


def At_function():
    clear()
    tk.Message(frame02,
               text='''Name: Astatine
Symbol: At
Atomic mass: 210 u
Atomic number: 85
Electron configuration: [Xe] 4f¹⁴5d¹⁰6s²6p⁵
Melting point: 302 °C
Boiling point: 336.8 °C
Van der Waals radius: 200 pm''').pack(anchor="w")


def Rn_function():
    clear()
    tk.Message(frame02,
               text='''Name: Radon
Symbol: Rn
Electrons per shell: 2,8,18,32,18,8
Atomic number: 86
Electron configuration: [Xe] 4f145d106s26p6
Boiling point: -61.7 °C
Melting point: -71 °C
Discovered: 1900''').pack(anchor="w")


def Fr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Francium
Symbol: Fr
Atomic mass: 223 u
Atomic number: 87
Electron configuration: [Rn] 7s1
Electronegativity: 0.79
Van der Waals radius: 348 pm
Melting point: 27 °C''').pack(anchor="w")


def Ra_function():
    clear()
    tk.Message(frame02,
               text='''Name: Radium
Symbol: Ra
Atomic mass: 226 u
Atomic number: 88
Discovered: December 21, 1898
Electron configuration: [Rn] 7s2
CAS ID: 7440-14-4
Discoverers: Marie Curie, Pierre Curie''').pack(anchor="w")


def Lr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Lawrencium
Symbol: Lr
Electron configuration: [Rn] 5f147s27p1
Atomic number: 103
Atomic mass: 262 u
Discovered: February 14, 1961
Van der Waals radius: 200 pm
Discoverer: Albert Ghiorso''').pack(anchor="w")


def Rf_function():
    clear()
    tk.Message(frame02,
               text='''Name: Rutherfordium
Symbol: Rf
Atomic number: 104
Electron configuration: [Rn] 5f146d27s2
Atomic mass: 261 u
Discovered: 1964
CAS ID: 53850-36-5
Discoverers: Joint Institute for Nuclear Research, Albert Ghiorso''').pack(
                   anchor="w")


def Db_function():
    clear()
    tk.Message(frame02,
               text='''Name: Dubnium
Symbol: Db
Atomic number: 105
Electron configuration: [Rn] 5f146d37s2
Atomic mass: 262 u
Discovered: 1967
Van der Waals radius: 200 pm
Discoverers: Joint Institute for Nuclear Research, Albert Ghiorso''').pack(
                   anchor="w")


def Sg_function():
    clear()
    tk.Message(frame02,
               text='''Name: Seaborgium
Symbol: Sg
Atomic number: 106
Discovered: 1974
Van der Waals radius: 200 pm
CAS ID: 54038-81-2
Naming: after Glenn T. Seaborg
Chemical series: Metal, Transition metal, Synthetic element, Period 7 element, Group 6 element'''
               ).pack(anchor="w")


def Bh_function():
    clear()
    tk.Message(frame02,
               text='''Name: Bohrium
Symbol: Bh
Atomic number: 107
Atomic mass: 264 u
Discovered: 1981
Van der Waals radius: 200 pm
CAS ID: 54037-14-8
Chemical series: Metal, Transition metal, Toxic heavy metal, Group 7 element, Period 7 element'''
               ).pack(anchor="w")


def Hs_function():
    clear()
    tk.Message(frame02,
               text='''Name: Hassium
Symbol: Hs
Atomic number: 108
Atomic mass: 277 u
Discovered: 1984
Van der Waals radius: 200 pm
CAS ID: 54037-57-9
Chemical series: Metal, Transition metal, Toxic heavy metal, Group 8 element, Period 7 element'''
               ).pack(anchor="w")


def Mt_function():
    clear()
    tk.Message(frame02,
               text='''Name: Meitnerium
Symbol: Mt
Atomic number: 109
Atomic mass: 278 u
Discovered: August 29, 1982
Van der Waals radius: 200 pm
CAS ID: 54038-01-6
Chemical series: Metal, Transition metal, Period 7 element, Group 9 element'''
               ).pack(anchor="w")


def Ds_function():
    clear()
    tk.Message(frame02,
               text='''Name: Darmstadtium
Symbol: Ds
Atomic number: 110
Atomic mass: 281 u
Discovered: 1994
CAS ID: 54083-77-1
Discoverer: Sigurd Hofmann
Chemical series: Metal, Transition metal, Period 7 element, Group 10 element'''
               ).pack(anchor="w")


def Rg_function():
    clear()
    tk.Message(frame02,
               text='''Name: Roentgenium
Symbol: Rg
Atomic number: 111
Atomic mass: 272 u
Discovered: December 8, 1994
CAS ID: 54386-24-2
Discoverers: Sigurd Hofmann, Victor Ninov
Chemical series: Metal, Transition metal, Period 7 element, Group 11 element'''
               ).pack(anchor="w")


def Cn_function():
    clear()
    tk.Message(frame02,
               text='''Name: Copernicium
Symbol: Cn
Atomic number: 112
Atomic mass: 285 u
Discovered: February 9, 1996
CAS ID: 54084-26-3
Discoverers: Sigurd Hofmann, Victor Ninov
Chemical series: Metal, Transition metal, Toxic heavy metal, Period 7 element, Group 12 element'''
               ).pack(anchor="w")


def Nh_function():
    clear()
    tk.Message(frame02,
               text='''Name: Nihonium
Symbol: Nh
Atomic mass: 286 u
Atomic number: 113
Discovered: 2003
CAS ID: 54084-70-7
Atomic radius: empirical: 170 pm (predicted)
Chemical series: Metal, Boron group, Period 7 element''').pack(anchor="w")


def Fl_function():
    clear()
    tk.Message(frame02,
               text='''Name: Flerovium
Symbol: Fl
Atomic number: 114
Atomic mass: 289 u
Discovered: December 1998
Electrons per shell: 2, 8, 18, 32, 32, 18, 4
Discoverers: Yuri Oganessian, Sigurd Hofmann, Flerov Laboratory of Nuclear Reactions
Chemical series: Metal, Carbon group, Period 7 element''').pack(anchor="w")


def Mc_function():
    clear()
    tk.Message(frame02,
               text='''Name: Moscovium
Symbol: Mc
Atomic number: 115
Discovered: 2003
Atomic mass: 288 u
CAS ID: 54085-64-2
Discoverer: Joint Institute for Nuclear Research
Chemical series: Metal, Pnictogen, Period 7 element''').pack(anchor="w")


def Lv_function():
    clear()
    tk.Message(frame02,
               text='''Name: Livermorium
Symbol: Lv
Atomic number: 116
Atomic mass: 292 u
Discovered: 2000
Electronegativity: 1.61
Discoverers: Yuri Oganessian, Joint Institute for Nuclear Research
Chemical series: Metal, Chalcogen, Period 7 element''').pack(anchor="w")


def Ts_function():
    clear()
    tk.Message(frame02,
               text='''Name: Tennessine
Symbol: Ts
Atomic number: 117
Discovered: April 5, 2010
CAS ID: 87658-56-8
Atomic radius: empirical: 138 pm (predicted)
Discoverers: Yuri Oganessian, Joint Institute for Nuclear Research
Chemical series: Halogen, Period 7 element''').pack(anchor="w")


def Og_function():
    clear()
    tk.Message(frame02,
               text='''Name: Oganesson
Symbol: Og
Atomic mass: 294 u
Atomic number: 118
Discovered: 2006
CAS ID: 54144-19-3
Discoverers: Yuri Oganessian, Joint Institute for Nuclear Research
Chemical series: Noble gas, Period 7 element''').pack(anchor="w")


def La_function():
    clear()
    tk.Message(frame02,
               text='''Name: Lanthanum
Symbol: La
Atomic mass: 138.90547 u
Electron configuration: [Xe] 5d¹6s²
Atomic number: 57
Discovered: 1839
Van der Waals radius: 250 pm
Melting point: 920 °C''').pack(anchor="w")


def Ce_function():
    clear()
    tk.Message(frame02,
               text='''Name: Cerium
Symbol: Ce
Atomic mass: 140.116 u
Atomic number: 58
Electron configuration: [Xe] 4f¹5d¹6s²
Van der Waals radius: 248 pm
CAS ID: 7440-45-1
Discovered: 1803''').pack(anchor="w")


def Pr_function():
    clear()
    tk.Message(frame02,
               text='''Name: Praseodymium
Symbol: Pr
Electron configuration: [Xe] 4f36s2
Discovered: 1885
Atomic number: 59
Atomic mass: 140.90765 u
CAS ID: 7440-10-0
Melting point: 931 °C''').pack(anchor="w")


def Nd_function():
    clear()
    tk.Message(frame02,
               text='''Name: Neodymium
Symbol: Nd
Electron configuration: [Xe] 4f⁴6s²
Atomic number: 60
Atomic mass: 144.242 u
Discovered: 1885
Van der Waals radius: 229 pm
CAS ID: 7440-00-8''').pack(anchor="w")


def Pm_function():
    clear()
    tk.Message(frame02,
               text='''Name: Promethium
Symbol: Pm
Atomic mass: 145 u
Electron configuration: [Xe] 4f56s2
Discovered: 1945
Atomic number: 61
CAS ID: 7440-12-2
Discoverers: Jacob A. Marinsky, Charles D. Coryell, Lawrence E. Glendenin'''
               ).pack(anchor="w")


def Sm_function():
    clear()
    tk.Message(frame02,
               text='''Name: Samarium
Symbol: Sm
Atomic mass: 150.36 u
Electron configuration: [Xe] 4f⁶6s²
Atomic number: 62
Discovered: 1879
Melting point: 1,072 °C
Discoverers: Paul-Émile Lecoq de Boisbaudran, Eugène-Anatole Demarçay''').pack(
                   anchor="w")


def Eu_function():
    clear()
    tk.Message(frame02,
               text='''Name: Europium
Symbol: Eu
Atomic mass: 151.964 u
Electron configuration: [Xe] 4f76s2
Atomic number: 63
Discovered: 1901
Van der Waals radius: 240 pm
Discoverers: Eugène-Anatole Demarçay, Paul-Émile Lecoq de Boisbaudran''').pack(
                   anchor="w")


def Gd_function():
    clear()
    tk.Message(frame02,
               text='''Name: Gadolinium
Symbol: Gd
Atomic mass: 157.25 u
Electron configuration: [Xe] 4f75d16s2
Atomic number: 64
Discovered: 1880
Van der Waals radius: 238 pm
Discoverers: Jean Charles Galissard de Marignac, Paul-Émile Lecoq de Boisbaudran'''
               ).pack(anchor="w")


def Tb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Terbium
Symbol: Tb
Atomic mass: 158.92535 u
Electron configuration: [Xe] 4f96s2
Atomic number: 65
Electrons per shell: 2,8,18,27,8,2
Discovered: 1843
Discoverer: Carl Gustaf Mosander''').pack(anchor="w")


def Dy_function():
    clear()
    tk.Message(frame02,
               text='''Name: Dysprosium
Symbol: Dy
Atomic mass: 162.5 u
Electron configuration: [Xe] 4f106s2
Atomic number: 66
Discovered: 1886
Van der Waals radius: 235 pm
Discoverer: Paul-Émile Lecoq de Boisbaudran''').pack(anchor="w")


def Ho_function():
    clear()
    tk.Message(frame02,
               text='''Name: Holmium
Symbol: Ho
Electrons per shell: 2,8,18,29,8,2
Electron configuration: [Xe] 4f116s2
Atomic number: 67
Atomic mass: 164.93032 u
Discovered: 1878
Discoverers: Per Teodor Cleve, Jacques-Louis Soret, Marc Delafontaine''').pack(
                   anchor="w")


def Er_function():
    clear()
    tk.Message(frame02,
               text='''Name: Erbium
Symbol: Er
Atomic mass: 167.259 u
Electron configuration: [Xe] 4f126s2
Atomic number: 68
CAS ID: 7440-52-0
Discovered: 1843
Van der Waals radius: 232 pm''').pack(anchor="w")


def Tm_function():
    clear()
    tk.Message(frame02,
               text='''Name: Thulium
Symbol: Tm
Atomic number: 69
Electron configuration: [Xe] 4f136s2
CAS ID: 7440-30-4
Atomic mass: 168.93421 u
Discovered: 1879
Discoverer: Per Teodor Cleve''').pack(anchor="w")


def Yb_function():
    clear()
    tk.Message(frame02,
               text='''Name: Ytterbium
Symbol: Yb
Atomic mass: 173.04 u
Electron : [Xe] 4f146s2
Atomic number: 70
CAS ID: 7440-64-4
Electrons per shell: 2,8,18,32,8,2
Discoverer: Jean Charles Galissard de Marignac''').pack(anchor="w")


def Ac_function():
    clear()
    tk.Message(frame02,
               text='''Name: Actinium
Symbol: Ac
Atomic number: 89
Electron configuration: [Rn] 6d17s2
Atomic mass: 227 u
CAS ID: 7440-34-8
Discovered: 1899
Discoverer: André-Louis Debierne''').pack(anchor="w")


def Th_function():
    clear()
    tk.Message(frame02,
               text='''Name: Thorium
Symbol: Th
Atomic mass: 232.03806 u
Atomic number: 90
Electron configuration: [Rn] 6d27s2
Discovered: 1828
Melting point: 1,750 °C
Discoverer: Jöns Jacob Berzelius''').pack(anchor="w")


def Pa_function():
    clear()
    tk.Message(frame02,
               text='''Symbol: Pa
Atomic number: 91
Electron configuration: [Rn] 5f26d17s2
CAS ID: 7440-13-3
Atomic mass: 231.03588 u
Melting point: 1,568 °C
Chemical series: Metal, Actinide, Toxic heavy metal, Period 7 element''').pack(
                   anchor="w")


def U_function():
    clear()
    tk.Message(frame02,
               text='''Name: Uranium
Symbol: U
Atomic mass: 238.02891 u
Electrons per shell: 2,8,18,32,21,9,2
Atomic number: 92
Electron configuration: [Rn] 5f36d17s2
Discovered: 1789
Discoverer: Martin Heinrich Klaproth''').pack(anchor="w")


def Np_function():
    clear()
    tk.Message(frame02,
               text='''Name: Neptunium
Symbol: Np
Atomic mass: 237.0482 u
Electron configuration: [Rn] 5f46d17s2
Atomic number: 93
CAS ID: 7439-99-8
Discovered: 1940
Discoverers: Edwin McMillan, Philip Abelson''').pack(anchor="w")


def Pu_function():
    clear()
    tk.Message(frame02,
               text='''Name: Plutonium
Symbol: Pu
Atomic mass: 244 u
Electrons per shell: 2,8,18,32,24,8,2
Atomic number: 94
Electron configuration: [Rn] 5f67s2
Discovered: December 14, 1940
Discoverers: Joseph W. Kennedy, Glenn T. Seaborg, Arthur Wahl, Edwin McMillan'''
               ).pack(anchor="w")


def Am_function():
    clear()
    tk.Message(frame02,
               text='''Name: Americium
Symbol: Am
Atomic mass: 243 u
Atomic number: 95
Electron configuration: [Rn] 5f77s2
Discovered: 1944
Discoverers: Glenn T. Seaborg, Albert Ghiorso, Ralph A. James
Chemical series: Metal, Actinide, Toxic heavy metal, Period 7 element''').pack(
                   anchor="w")


def Cm_function():
    clear()
    tk.Message(frame02,
               text='''Name: Curium
Symbol: Cm
Electron configuration: [Rn] 5f76d17s2
Atomic number: 96
Atomic mass: 247 u
Discovered: 1944
Melting point: 1,345 °C
Discoverers: Glenn T. Seaborg, Albert Ghiorso, Ralph A. James''').pack(
                   anchor="w")


def Bk_function():
    clear()
    tk.Message(frame02,
               text='''Name: Berkelium
Symbol: Bk
Electron configuration: [Rn] 5f97s2
Atomic number: 97
Atomic mass: 247 u
Discovered: 1949
Van der Waals radius: 200 pm
Discoverers: Glenn T. Seaborg, Albert Ghiorso''').pack(anchor="w")


def Cf_function():
    clear()
    tk.Message(frame02,
               text='''Name: Californium
Symbol: Cf
Atomic number: 98
Electron configuration: [Rn] 5f107s2
Atomic mass: 251 u
Discovered: March 17, 1950
Melting point: 900 °C
Discoverers: Glenn T. Seaborg, Albert Ghiorso''').pack(anchor="w")


def Es_function():
    clear()
    tk.Message(frame02,
               text='''Name: Einsteinium
Symbol: Es
Atomic number: 99
Electron configuration: [Rn] 5f117s2
Atomic mass: 252 u
Discovered: December 1952
Electrons per shell: 2, 8, 18, 32, 29, 8, 2
Discoverers: Glenn T. Seaborg, Albert Ghiorso''').pack(anchor="w")


def Fm_function():
    clear()
    tk.Message(frame02,
               text='''Name: Fermium
Symbol: Fm
Electrons per shell: 2,8,18,32,30,8,2
Atomic number: 100
Electron configuration: [Rn] 5f127s2
Atomic mass: 257 u
Discovered: 1953
Discoverers: Glenn T. Seaborg, Albert Ghiorso''').pack(anchor="w")


def Md_function():
    clear()
    tk.Message(frame02,
               text='''Name: Mendelevium
Symbol: Md
Atomic number: 101
Electron configuration: [Rn] 5f137s2
Atomic mass: 258 u
CAS ID: 7440-11-1
Discovered: 1955
Discoverers: Glenn T. Seaborg, Albert Ghiorso''').pack(anchor="w")


def No_function():
    clear()
    tk.Message(frame02,
               text='''Name: Nobelium
Symbol: No
Electron configuration: [Rn] 5f147s2
Atomic number: 102
Atomic mass: 259 u
CAS ID: 10028-14-5
Discovered: 1958
Discoverers: Glenn T. Seaborg, Joint Institute for Nuclear Research''').pack(
                   anchor="w")


# Creating Keys
Non_Metals = tk.Label(key_frame,
                      text="Non-Metals",
                      font=("Helvetica", 8),
                      bg="#319ffe")
Non_Metals.grid(row=0, column=1, padx=(0, 5), pady=5)

Noble_Gases = tk.Label(key_frame,
                       text="Noble Gases",
                       font=("Helvetica", 8),
                       bg="#febd01")
Noble_Gases.grid(row=0, column=2, padx=5, pady=5)

Alkali_Metals = tk.Label(key_frame,
                         text="Alkali Metals",
                         font=("Helvetica", 8),
                         bg="#f400fe")
Alkali_Metals.grid(row=0, column=3, padx=5, pady=5)

Alkaline_Earth_Metals = tk.Label(key_frame,
                                 text="Alkaline Earth Metals",
                                 font=("Helvetica", 8),
                                 bg="#aa4dfe")
Alkaline_Earth_Metals.grid(row=0, column=4, padx=5, pady=5)

Semimetals = tk.Label(key_frame,
                      text="Semimetals",
                      font=("Helvetica", 8),
                      bg="#02e76b")
Semimetals.grid(row=0, column=5, padx=5, pady=5)

Halogens = tk.Label(key_frame,
                    text="Halogens",
                    font=("Helvetica", 8),
                    bg="#c5bd24")
Halogens.grid(row=0, column=6, padx=5, pady=5)

Basic_Metals = tk.Label(key_frame,
                        text="Basic Metals",
                        font=("Helvetica", 8),
                        bg="#fe6f40")
Basic_Metals.grid(row=0, column=7, padx=5, pady=5)

Transition_Metals = tk.Label(key_frame,
                             text="Transition Metals",
                             font=("Helvetica", 8),
                             bg="#33d3fe")
Transition_Metals.grid(row=0, column=8, padx=5, pady=5)

Lanthanide = tk.Label(key_frame,
                      text="Lanthanide",
                      font=("Helvetica", 8),
                      bg="#baff2a")
Lanthanide.grid(row=0, column=9, padx=5, pady=5)

Actinide = tk.Label(key_frame,
                    text="Actinide",
                    font=("Helvetica", 8),
                    bg="#fe2120")
Actinide.grid(row=0, column=10, padx=(5, 10), pady=5)

for i in range(10):
    key_frame.grid_columnconfigure(i, weight=1)

# Creating Periods & Groups

G1 = tk.Message(frame01, text="1\nIA", font=("Helvetica", 7))
G1.grid(row=0, column=1)

G2 = tk.Message(frame01, text="2\nIIA", font=("Helvetica", 7))
G2.grid(row=0, column=2)

G3 = tk.Message(frame01, text="3\nIIIB", font=("Helvetica", 7))
G3.grid(row=0, column=3)

G4 = tk.Message(frame01, text="4\nIVB", font=("Helvetica", 7))
G4.grid(row=0, column=4)

G5 = tk.Message(frame01, text="5\nVB", font=("Helvetica", 7))
G5.grid(row=0, column=5)

G6 = tk.Message(frame01, text="6\nVIB", font=("Helvetica", 7))
G6.grid(row=0, column=6)

G7 = tk.Message(frame01, text="7\nVIIB", font=("Helvetica", 7))
G7.grid(row=0, column=7)

G8 = tk.Message(frame01, text="8\nVIIIB", font=("Helvetica", 7))
G8.grid(row=0, column=8)

G9 = tk.Message(frame01, text="9\nVIIIB", font=("Helvetica", 7))
G9.grid(row=0, column=9)

G10 = tk.Message(frame01, text="10\nVIIIB", font=("Helvetica", 7))
G10.grid(row=0, column=10)

G11 = tk.Message(frame01, text="11\nIB", font=("Helvetica", 7))
G11.grid(row=0, column=11)

G12 = tk.Message(frame01, text="12\nIIB", font=("Helvetica", 7))
G12.grid(row=0, column=12)

G13 = tk.Message(frame01, text="13\nIIIA", font=("Helvetica", 7))
G13.grid(row=0, column=13)

G14 = tk.Message(frame01, text="14\nIVA", font=("Helvetica", 7))
G14.grid(row=0, column=14)

G15 = tk.Message(frame01, text="15\nVA", font=("Helvetica", 7))
G15.grid(row=0, column=15)

G16 = tk.Message(frame01, text="16\nVIA", font=("Helvetica", 7))
G16.grid(row=0, column=16)

G17 = tk.Message(frame01, text="17\nVIIA", font=("Helvetica", 7))
G17.grid(row=0, column=17)

G18 = tk.Message(frame01, text="18\nVIIIA", font=("Helvetica", 7))
G18.grid(row=0, column=18)

P1 = tk.Message(frame01, text="1", font=("Helvetica", 7))
P1.grid(row=1, column=0)

P1 = tk.Message(frame01, text="2", font=("Helvetica", 7))
P1.grid(row=2, column=0)

P1 = tk.Message(frame01, text="3", font=("Helvetica", 7))
P1.grid(row=3, column=0)

P1 = tk.Message(frame01, text="4", font=("Helvetica", 7))
P1.grid(row=4, column=0)

P1 = tk.Message(frame01, text="5", font=("Helvetica", 7))
P1.grid(row=5, column=0)

P1 = tk.Message(frame01, text="6", font=("Helvetica", 7))
P1.grid(row=6, column=0)

P1 = tk.Message(frame01, text="7", font=("Helvetica", 7))
P1.grid(row=7, column=0)

# Creating Elements Buttons

H_button = tk.Button(frame01,
                     text="H",
                     width=2,
                     bg="#319ffe",
                     command=H_function)
H_button.grid(row=1, column=1)

He_button = tk.Button(frame01,
                      text="He",
                      width=2,
                      bg="#febd01",
                      command=He_function)
He_button.grid(row=1, column=18)

Li_button = tk.Button(frame01,
                      text="Li",
                      width=2,
                      bg="#f400fe",
                      command=Li_function)
Li_button.grid(row=2, column=1)

Be_button = tk.Button(frame01,
                      text="Be",
                      width=2,
                      bg="#aa4dfe",
                      command=Be_function)
Be_button.grid(row=2, column=2, padx=(0, 5))

B_button = tk.Button(frame01,
                     text="B",
                     width=2,
                     bg="#02e76b",
                     command=B_function)
B_button.grid(row=2, column=13)

C_button = tk.Button(frame01,
                     text="C",
                     width=2,
                     bg="#319ffe",
                     command=C_function)
C_button.grid(row=2, column=14)

N_button = tk.Button(frame01,
                     text="N",
                     width=2,
                     bg="#319ffe",
                     command=N_function)
N_button.grid(row=2, column=15)

O_button = tk.Button(frame01,
                     text="O",
                     width=2,
                     bg="#319ffe",
                     command=O_function)
O_button.grid(row=2, column=16)

F_button = tk.Button(frame01,
                     text="F",
                     width=2,
                     bg="#c5bd24",
                     command=F_function)
F_button.grid(row=2, column=17)

Ne_button = tk.Button(frame01,
                      text="Ne",
                      width=2,
                      bg="#febd01",
                      command=Ne_function)
Ne_button.grid(row=2, column=18)

Na_button = tk.Button(frame01,
                      text="Na",
                      width=2,
                      bg="#f400fe",
                      command=Na_function)
Na_button.grid(row=3, column=1)

Mg_button = tk.Button(frame01,
                      text="Mg",
                      width=2,
                      bg="#aa4dfe",
                      command=Mg_function)
Mg_button.grid(row=3, column=2, padx=(0, 5))

Al_button = tk.Button(frame01,
                      text="Al",
                      width=2,
                      bg="#fe6f40",
                      command=Al_function)
Al_button.grid(row=3, column=13)

Si_button = tk.Button(frame01,
                      text="Si",
                      width=2,
                      bg="#02e76b",
                      command=Si_function)
Si_button.grid(row=3, column=14)

P_button = tk.Button(frame01,
                     text="P",
                     width=2,
                     bg="#319ffe",
                     command=P_function)
P_button.grid(row=3, column=15)

S_button = tk.Button(frame01,
                     text="S",
                     width=2,
                     bg="#319ffe",
                     command=S_function)
S_button.grid(row=3, column=16)

Cl_button = tk.Button(frame01,
                      text="Cl",
                      width=2,
                      bg="#c5bd24",
                      command=Cl_function)
Cl_button.grid(row=3, column=17)

Ar_button = tk.Button(frame01,
                      text="Ar",
                      width=2,
                      bg="#febd01",
                      command=Ar_function)
Ar_button.grid(row=3, column=18)

K_button = tk.Button(frame01,
                     text="K",
                     width=2,
                     bg="#f400fe",
                     command=K_function)
K_button.grid(row=4, column=1)

Ca_button = tk.Button(frame01,
                      text="Ca",
                      width=2,
                      bg="#aa4dfe",
                      command=Ca_function)
Ca_button.grid(row=4, column=2, padx=(0, 5))

Sc_button = tk.Button(frame01,
                      text="Sc",
                      width=2,
                      bg="#33d3fe",
                      command=Sc_function)
Sc_button.grid(row=4, column=3)

Ti_button = tk.Button(frame01,
                      text="Ti",
                      width=2,
                      bg="#33d3fe",
                      command=Ti_function)
Ti_button.grid(row=4, column=4)

V_button = tk.Button(frame01,
                     text="V",
                     width=2,
                     bg="#33d3fe",
                     command=V_function)
V_button.grid(row=4, column=5)

Cr_button = tk.Button(frame01,
                      text="Cr",
                      width=2,
                      bg="#33d3fe",
                      command=Cr_function)
Cr_button.grid(row=4, column=6)

Mn_button = tk.Button(frame01,
                      text="Mn",
                      width=2,
                      bg="#33d3fe",
                      command=Mn_function)
Mn_button.grid(row=4, column=7)

Fe_button = tk.Button(frame01,
                      text="Fe",
                      width=2,
                      bg="#33d3fe",
                      command=Fe_function)
Fe_button.grid(row=4, column=8)

Co_button = tk.Button(frame01,
                      text="Co",
                      width=2,
                      bg="#33d3fe",
                      command=Co_function)
Co_button.grid(row=4, column=9)

Ni_button = tk.Button(frame01,
                      text="Ni",
                      width=2,
                      bg="#33d3fe",
                      command=Ni_function)
Ni_button.grid(row=4, column=10)

Cu_button = tk.Button(frame01,
                      text="Cu",
                      width=2,
                      bg="#33d3fe",
                      command=Cu_function)
Cu_button.grid(row=4, column=11)

Zn_button = tk.Button(frame01,
                      text="Zn",
                      width=2,
                      bg="#33d3fe",
                      command=Zn_function)
Zn_button.grid(row=4, column=12)

Ga_button = tk.Button(frame01,
                      text="Ga",
                      width=2,
                      bg="#fe6f40",
                      command=Ga_function)
Ga_button.grid(row=4, column=13)

Ge_button = tk.Button(frame01,
                      text="Ge",
                      width=2,
                      bg="#02e76b",
                      command=Ge_function)
Ge_button.grid(row=4, column=14)

As_button = tk.Button(frame01,
                      text="As",
                      width=2,
                      bg="#02e76b",
                      command=As_function)
As_button.grid(row=4, column=15)

Se_button = tk.Button(frame01,
                      text="Se",
                      width=2,
                      bg="#319ffe",
                      command=Se_function)
Se_button.grid(row=4, column=16)

Br_button = tk.Button(frame01,
                      text="Br",
                      width=2,
                      bg="#c5bd24",
                      command=Br_function)
Br_button.grid(row=4, column=17)

Kr_button = tk.Button(frame01,
                      text="Kr",
                      width=2,
                      bg="#febd01",
                      command=Kr_function)
Kr_button.grid(row=4, column=18)

Rb_button = tk.Button(frame01,
                      text="Rb",
                      width=2,
                      bg="#f400fe",
                      command=Rb_function)
Rb_button.grid(row=5, column=1)

Sr_button = tk.Button(frame01,
                      text="Sr",
                      width=2,
                      bg="#aa4dfe",
                      command=Sr_function)
Sr_button.grid(row=5, column=2, padx=(0, 5))

Y_button = tk.Button(frame01,
                     text="Y",
                     width=2,
                     bg="#33d3fe",
                     command=Y_function)
Y_button.grid(row=5, column=3)

Zr_button = tk.Button(frame01,
                      text="Zr",
                      width=2,
                      bg="#33d3fe",
                      command=Zr_function)
Zr_button.grid(row=5, column=4)

Nb_button = tk.Button(frame01,
                      text="Nb",
                      width=2,
                      bg="#33d3fe",
                      command=Nb_function)
Nb_button.grid(row=5, column=5)

Mo_button = tk.Button(frame01,
                      text="Mo",
                      width=2,
                      bg="#33d3fe",
                      command=Mo_function)
Mo_button.grid(row=5, column=6)

Tc_button = tk.Button(frame01,
                      text="Tc",
                      width=2,
                      bg="#33d3fe",
                      command=Tc_function)
Tc_button.grid(row=5, column=7)

Ru_button = tk.Button(frame01,
                      text="Ru",
                      width=2,
                      bg="#33d3fe",
                      command=Ru_function)
Ru_button.grid(row=5, column=8)

Rh_button = tk.Button(frame01,
                      text="Rh",
                      width=2,
                      bg="#33d3fe",
                      command=Rh_function)
Rh_button.grid(row=5, column=9)

Pd_button = tk.Button(frame01,
                      text="Pd",
                      width=2,
                      bg="#33d3fe",
                      command=Pd_function)
Pd_button.grid(row=5, column=10)

Ag_button = tk.Button(frame01,
                      text="Ag",
                      width=2,
                      bg="#33d3fe",
                      command=Ag_function)
Ag_button.grid(row=5, column=11)

Cd_button = tk.Button(frame01,
                      text="Cd",
                      width=2,
                      bg="#33d3fe",
                      command=Cd_function)
Cd_button.grid(row=5, column=12)

In_button = tk.Button(frame01,
                      text="In",
                      width=2,
                      bg="#fe6f40",
                      command=In_function)
In_button.grid(row=5, column=13)

Sn_button = tk.Button(frame01,
                      text="Sn",
                      width=2,
                      bg="#fe6f40",
                      command=Sn_function)
Sn_button.grid(row=5, column=14)

Sb_button = tk.Button(frame01,
                      text="Sb",
                      width=2,
                      bg="#02e76b",
                      command=Sb_function)
Sb_button.grid(row=5, column=15)

Te_button = tk.Button(frame01,
                      text="Te",
                      width=2,
                      bg="#02e76b",
                      command=Te_function)
Te_button.grid(row=5, column=16)

I_button = tk.Button(frame01,
                     text="I",
                     width=2,
                     bg="#c5bd24",
                     command=I_function)
I_button.grid(row=5, column=17)

Xe_button = tk.Button(frame01,
                      text="Xe",
                      width=2,
                      bg="#febd01",
                      command=Xe_function)
Xe_button.grid(row=5, column=18)

Cs_button = tk.Button(frame01,
                      text="Cs",
                      width=2,
                      bg="#f400fe",
                      command=Cs_function)
Cs_button.grid(row=6, column=1)

Ba_button = tk.Button(frame01,
                      text="Ba",
                      width=2,
                      bg="#aa4dfe",
                      command=Ba_function)
Ba_button.grid(row=6, column=2, padx=(0, 5))

Lu_button = tk.Button(frame01,
                      text="Lu",
                      width=2,
                      bg="#baff2a",
                      command=Lu_function)
Lu_button.grid(row=6, column=3)

Hf_button = tk.Button(frame01,
                      text="Hf",
                      width=2,
                      bg="#33d3fe",
                      command=Hf_function)
Hf_button.grid(row=6, column=4)

Ta_button = tk.Button(frame01,
                      text="Ta",
                      width=2,
                      bg="#33d3fe",
                      command=Ta_function)
Ta_button.grid(row=6, column=5)

W_button = tk.Button(frame01,
                     text="W",
                     width=2,
                     bg="#33d3fe",
                     command=W_function)
W_button.grid(row=6, column=6)

Re_button = tk.Button(frame01,
                      text="Re",
                      width=2,
                      bg="#33d3fe",
                      command=Re_function)
Re_button.grid(row=6, column=7)

Os_button = tk.Button(frame01,
                      text="Os",
                      width=2,
                      bg="#33d3fe",
                      command=Os_function)
Os_button.grid(row=6, column=8)

Ir_button = tk.Button(frame01,
                      text="Ir",
                      width=2,
                      bg="#33d3fe",
                      command=Ir_function)
Ir_button.grid(row=6, column=9)

Pt_button = tk.Button(frame01,
                      text="Pt",
                      width=2,
                      bg="#33d3fe",
                      command=Pt_function)
Pt_button.grid(row=6, column=10)

Au_button = tk.Button(frame01,
                      text="Au",
                      width=2,
                      bg="#33d3fe",
                      command=Au_function)
Au_button.grid(row=6, column=11)

Hg_button = tk.Button(frame01,
                      text="Hg",
                      width=2,
                      bg="#33d3fe",
                      command=Hg_function)
Hg_button.grid(row=6, column=12)

Tl_button = tk.Button(frame01,
                      text="Tl",
                      width=2,
                      bg="#fe6f40",
                      command=Tl_function)
Tl_button.grid(row=6, column=13)

Pb_button = tk.Button(frame01,
                      text="Pb",
                      width=2,
                      bg="#fe6f40",
                      command=Pb_function)
Pb_button.grid(row=6, column=14)

Bi_button = tk.Button(frame01,
                      text="Bi",
                      width=2,
                      bg="#fe6f40",
                      command=Bi_function)
Bi_button.grid(row=6, column=15)

Po_button = tk.Button(frame01,
                      text="Po",
                      width=2,
                      bg="#02e76b",
                      command=Po_function)
Po_button.grid(row=6, column=16)

At_button = tk.Button(frame01,
                      text="At",
                      width=2,
                      bg="#c5bd24",
                      command=At_function)
At_button.grid(row=6, column=17)

Rn_button = tk.Button(frame01,
                      text="Rn",
                      width=2,
                      bg="#febd01",
                      command=Rn_function)
Rn_button.grid(row=6, column=18)

Fr_button = tk.Button(frame01,
                      text="Fr",
                      width=2,
                      bg="#f400fe",
                      command=Fr_function)
Fr_button.grid(row=7, column=1)

Ra_button = tk.Button(frame01,
                      text="Ra",
                      width=2,
                      bg="#aa4dfe",
                      command=Ra_function)
Ra_button.grid(row=7, column=2, padx=(0, 5))

Lr_button = tk.Button(frame01,
                      text="Lr",
                      width=2,
                      bg="#fe2120",
                      command=Lr_function)
Lr_button.grid(row=7, column=3)

Rf_button = tk.Button(frame01,
                      text="Rf",
                      width=2,
                      bg="#33d3fe",
                      command=Rf_function)
Rf_button.grid(row=7, column=4)

Db_button = tk.Button(frame01,
                      text="Db",
                      width=2,
                      bg="#33d3fe",
                      command=Db_function)
Db_button.grid(row=7, column=5)

Sg_button = tk.Button(frame01,
                      text="Sg",
                      width=2,
                      bg="#33d3fe",
                      command=Sg_function)
Sg_button.grid(row=7, column=6)

Bh_button = tk.Button(frame01,
                      text="Bh",
                      width=2,
                      bg="#33d3fe",
                      command=Bh_function)
Bh_button.grid(row=7, column=7)

Hs_button = tk.Button(frame01,
                      text="Hs",
                      width=2,
                      bg="#33d3fe",
                      command=Hs_function)
Hs_button.grid(row=7, column=8)

Mt_button = tk.Button(frame01,
                      text="Mt",
                      width=2,
                      bg="#33d3fe",
                      command=Mt_function)
Mt_button.grid(row=7, column=9)

Ds_button = tk.Button(frame01,
                      text="Ds",
                      width=2,
                      bg="#33d3fe",
                      command=Ds_function)
Ds_button.grid(row=7, column=10)

Rg_button = tk.Button(frame01,
                      text="Rg",
                      width=2,
                      bg="#33d3fe",
                      command=Rg_function)
Rg_button.grid(row=7, column=11)

Cn_button = tk.Button(frame01,
                      text="Cn",
                      width=2,
                      bg="#33d3fe",
                      command=Cn_function)
Cn_button.grid(row=7, column=12)

Nh_button = tk.Button(frame01,
                      text="Nh",
                      width=2,
                      bg="#fe6f40",
                      command=Nh_function)
Nh_button.grid(row=7, column=13)

Fl_button = tk.Button(frame01,
                      text="Fl",
                      width=2,
                      bg="#fe6f40",
                      command=Fl_function)
Fl_button.grid(row=7, column=14)

Mc_button = tk.Button(frame01,
                      text="Mc",
                      width=2,
                      bg="#fe6f40",
                      command=Mc_function)
Mc_button.grid(row=7, column=15)

Lv_button = tk.Button(frame01,
                      text="Lv",
                      width=2,
                      bg="#fe6f40",
                      command=Lv_function)
Lv_button.grid(row=7, column=16)

Ts_button = tk.Button(frame01,
                      text="Ts",
                      width=2,
                      bg="#c5bd24",
                      command=Ts_function)
Ts_button.grid(row=7, column=17)

Og_button = tk.Button(frame01,
                      text="Og",
                      width=2,
                      bg="#febd01",
                      command=Og_function)
Og_button.grid(row=7, column=18)

La_button = tk.Button(frame01,
                      text="La",
                      width=2,
                      bg="#baff2a",
                      command=La_function)
La_button.grid(row=8, column=3, pady=(5, 0))

Ce_button = tk.Button(frame01,
                      text="Ce",
                      width=2,
                      bg="#baff2a",
                      command=Ce_function)
Ce_button.grid(row=8, column=4, pady=(5, 0))

Pr_button = tk.Button(frame01,
                      text="Pr",
                      width=2,
                      bg="#baff2a",
                      command=Pr_function)
Pr_button.grid(row=8, column=5, pady=(5, 0))

Nd_button = tk.Button(frame01,
                      text="Nd",
                      width=2,
                      bg="#baff2a",
                      command=Nd_function)
Nd_button.grid(row=8, column=6, pady=(5, 0))

Pm_button = tk.Button(frame01,
                      text="Pm",
                      width=2,
                      bg="#baff2a",
                      command=Pm_function)
Pm_button.grid(row=8, column=7, pady=(5, 0))

Sm_button = tk.Button(frame01,
                      text="Sm",
                      width=2,
                      bg="#baff2a",
                      command=Sm_function)
Sm_button.grid(row=8, column=8, pady=(5, 0))

Eu_button = tk.Button(frame01,
                      text="Eu",
                      width=2,
                      bg="#baff2a",
                      command=Eu_function)
Eu_button.grid(row=8, column=9, pady=(5, 0))

Gd_button = tk.Button(frame01,
                      text="Gd",
                      width=2,
                      bg="#baff2a",
                      command=Gd_function)
Gd_button.grid(row=8, column=10, pady=(5, 0))

Tb_button = tk.Button(frame01,
                      text="Tb",
                      width=2,
                      bg="#baff2a",
                      command=Tb_function)
Tb_button.grid(row=8, column=11, pady=(5, 0))

Dy_button = tk.Button(frame01,
                      text="Dy",
                      width=2,
                      bg="#baff2a",
                      command=Dy_function)
Dy_button.grid(row=8, column=12, pady=(5, 0))

Ho_button = tk.Button(frame01,
                      text="Ho",
                      width=2,
                      bg="#baff2a",
                      command=Ho_function)
Ho_button.grid(row=8, column=13, pady=(5, 0))

Er_button = tk.Button(frame01,
                      text="Er",
                      width=2,
                      bg="#baff2a",
                      command=Er_function)
Er_button.grid(row=8, column=14, pady=(5, 0))

Tm_button = tk.Button(frame01,
                      text="Tm",
                      width=2,
                      bg="#baff2a",
                      command=Tm_function)
Tm_button.grid(row=8, column=15, pady=(5, 0))

Yb_button = tk.Button(frame01,
                      text="Yb",
                      width=2,
                      bg="#baff2a",
                      command=Yb_function)
Yb_button.grid(row=8, column=16, pady=(5, 0))

Ac_button = tk.Button(frame01,
                      text="Ac",
                      width=2,
                      bg="#fe2120",
                      command=Ac_function)
Ac_button.grid(row=9, column=3)

Th_button = tk.Button(frame01,
                      text="Th",
                      width=2,
                      bg="#fe2120",
                      command=Th_function)
Th_button.grid(row=9, column=4)

Pa_button = tk.Button(frame01,
                      text="Pa",
                      width=2,
                      bg="#fe2120",
                      command=Pa_function)
Pa_button.grid(row=9, column=5)

U_button = tk.Button(frame01,
                     text="U",
                     width=2,
                     bg="#fe2120",
                     command=U_function)
U_button.grid(row=9, column=6)

Np_button = tk.Button(frame01,
                      text="Np",
                      width=2,
                      bg="#fe2120",
                      command=Np_function)
Np_button.grid(row=9, column=7)

Pu_button = tk.Button(frame01,
                      text="Pu",
                      width=2,
                      bg="#fe2120",
                      command=Pu_function)
Pu_button.grid(row=9, column=8)

Am_button = tk.Button(frame01,
                      text="Am",
                      width=2,
                      bg="#fe2120",
                      command=Am_function)
Am_button.grid(row=9, column=9)

Cm_button = tk.Button(frame01,
                      text="Cm",
                      width=2,
                      bg="#fe2120",
                      command=Cm_function)
Cm_button.grid(row=9, column=10)

Bk_button = tk.Button(frame01,
                      text="Bk",
                      width=2,
                      bg="#fe2120",
                      command=Bk_function)
Bk_button.grid(row=9, column=11)

Cf_button = tk.Button(frame01,
                      text="Cf",
                      width=2,
                      bg="#fe2120",
                      command=Cf_function)
Cf_button.grid(row=9, column=12)

Es_button = tk.Button(frame01,
                      text="Es",
                      width=2,
                      bg="#fe2120",
                      command=Es_function)
Es_button.grid(row=9, column=13)

Fm_button = tk.Button(frame01,
                      text="Fm",
                      width=2,
                      bg="#fe2120",
                      command=Fm_function)
Fm_button.grid(row=9, column=14)

Md_button = tk.Button(frame01,
                      text="Md",
                      width=2,
                      bg="#fe2120",
                      command=Md_function)
Md_button.grid(row=9, column=15)

No_button = tk.Button(frame01,
                      text="No",
                      width=2,
                      bg="#fe2120",
                      command=No_function)
No_button.grid(row=9, column=16)

tk.mainloop()
