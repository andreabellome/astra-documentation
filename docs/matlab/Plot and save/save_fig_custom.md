# `save_fig_custom`

## DESCRIPTION
This function saves a given MATLAB figure in either PDF or SVG format with
specified resolution and filename. It adjusts the figure’s paper size to
match the on-screen size for high-quality export. Default values are used
when fewer than four input arguments are provided.

## INPUT
- fig                   : handle to the figure to be saved. If not provided,
the current figure (gcf) is used.
- dpi                   : resolution in dots per inch (DPI) for export.
Default is 600.
- type                  : string specifying the file type ('pdf' or 'svg').
Default is 'pdf'.
- name_including_folder : full name of the file including folder and extension.
The extension must match the specified type.

## OUTPUT
- none : the figure is saved to file in the specified format and resolution.

