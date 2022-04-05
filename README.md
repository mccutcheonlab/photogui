# photogui
This package contains code to launch GUIs for analysing photometry data. There are separate versions that handle data collected via Tucker Davis Technologies (TDT) systems and Neurophotometrics systems.

Code is maintained by James McCutcheon, Dept of Psychology, UiT The Arctic University of Norway.

## Installation

 The GUI has not been uploaded to pip yet but can be easily installed at the command line (e.g. at an Anaconda prompt).
```
 python -m pip install git+https://github.com/mccutcheonlab/photogui.git
```
 If it does not work make sure that you have git installed.
```
 conda install git
```
 Once installed the GUIs can be launched by starting a python session
```
 python
```
 and importing the package and running one of the following functions

```
>>> import photogui as pg
>>> pg.start_photo_gui()
```


or
```
>>> import photogui as pg
>>> pg.start_photo_gui_np()
```
If you want tips for how to use the GUIs you can include the option, `quickstart=True`, e.g.
```
>>> pg.start_photo_gui(quickstart=True)
```
If you are interested in the functions that are used to process signals then I encourage you to check out the `trompy` package where they can all be examined. This package can be installed via pip.
```
pip install trompy
```

## How to cite this project?

Please email jmc010@uit.no to get instructions on how to properly cite this project.

## Contributing

You are welcome to contribute to the code via pull requests. Please have a look at the NLeSC guide for guidelines about software development.

