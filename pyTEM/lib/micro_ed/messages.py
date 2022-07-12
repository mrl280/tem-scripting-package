"""
 Author:  Michael Luciuk
 Date:    Summer 2022
"""

import tkinter as tk
from tkinter import ttk
from typing import Tuple, Union

from pyTEM.Interface import Interface
from pyTEM.lib.micro_ed.add_basf_icon_to_tkinter_window import add_basf_icon_to_tkinter_window
from pyTEM.lib.micro_ed.exit_script import exit_script


def get_welcome_message() -> Tuple[str, str]:
    """
    :return: str: A welcome message.
    """
    title = "Good afternoon ladies and gentlemen. This is the pre-boarding announcement for TEM Air flight M300 with " \
            "service to Ludwigshafen am Rhein."
    message = "Welcome to BASF's in-house micro-crystal electron diffraction (MicroED) automated imaging " \
              "script. MicroED allows fast, high resolution 3D structure determination of small chemical " \
              "compounds biological macromolecules! You can exit the script any time using the exit buttons on the " \
              "pop-up message boxes, or by hitting Ctrl-C on your keyboard. " \
              "\n\nPlease click the Continue button to get started!"
    return title, message


def get_initialization_message() -> Tuple[str, str]:
    """
    :return: str: Initialization/connection message.
    """
    title = "We are now inviting those passengers with small children, and any passengers requiring special " \
            "assistance, to begin boarding at gate 7 at this time."
    message = "In order to initialize the microscope for MicroED, we are now going to: " \
              "\n - Insert the Flucam screen." \
              "\n - Make sure the microscope is in 'TEM' mode." \
              "\n - Make sure the microscope is in 'imaging' mode. " \
              "\n - Zero the image shift." \
              "\n - Zero the \u03B1 tilt." \
              "\n - Normalize all lenses." \
              "\n - Unblank the beam." \
              "\n\nIf a chosen particle has already been identified, you may want to reduce the illumination and " \
              "move the stage such that it will not be illuminated once, upon completion of the initialization " \
              "process, we unblank the beam." \
              "\n\nOnce you are ready to start the initialization procedure, please click the Continue button."
    return title, message


def get_find_dummy_particle_message() -> Tuple[str, str]:
    """
    :return: str: An message prompting the user to find the dummy particle.
    """
    title = "We are now inviting our business and first-class customers to gate 7 for priority boarding."
    message = "Using the microscope control panel, please select a magnification in the SA range and center the " \
              "microscope on some dummy particle. Don't worry about over-exposing the particle, this is the not the " \
              "particle we are going to analyse. For best results, please choose a dummy particle at approximately " \
              "the same y-location as (and preferably near to) the particle you want to analyse." \
              "\n\nPlease do not adjust the stage tilt nor the image shift. " \
              "\n\nOnce the dummy particle is centered, please click the Continue button."
    return title, message


def get_eucentric_height_message() -> Tuple[str, str]:
    """
    :return: str: An eucentric height message.
    """
    title = "We will now begin general boarding for TEM Air flight M300 with service to Ludwigshafen am Rhein."
    message = "Please, using the \u03B1 wobble and z-axis buttons on the microscope control panel, manually set the " \
              "microscope to the eucentric height. That is, please find and select the z-height where tilting the " \
              "specimen leads to a minimal lateral movement of the image." \
              "\n\nOnce at eucentric height, re-center on the dummy particle and click the Continue button."
    return title, message


def get_alignment_message() -> Tuple[str, str]:
    """
    :return: str: An alignment message.
    """
    title = "Our flight is now ready for departure, we wish you all an enjoyable flight."
    message = "Using the microscope control panel, please (still with a magnification in the SA range) center the " \
              "microscope on the particle of interest. " \
              "\n\nPlease do not adjust the stage tilt nor the image shift. " \
              "\n\nOnce the particle is centered, please click the Continue button and the blanker will be " \
              "enabled automatically."
    return title, message


def automated_alignment_message() -> Tuple[str, str]:
    """
    :return: str: A message explaining the automated image alignment functionality.
    """
    title = "If you have any questions, please don’t hesitate to ask one of our crew members."
    message = "This MicroED script supports automated image alignment functionality. The required image shifts will " \
              "be computed from a preparatory tilt sequence using the hyperspy Python library (phase correlation) " \
              "and then applied during the main acquisition sequence. While automated image alignment can be useful, " \
              "it increases sample exposure time (although usually not significantly)." \
              "\n\nTo continue without image alignment functionality, please uncheck the checkbox below."
    return title, message


def get_insert_and_align_sad_aperture_message() -> Tuple[str, str]:
    """
    :return: str: A message prompting the user to insert and align the selected area diffraction (SAD) aperture.
    """
    title = "In order to expedite the boarding process, please be seated as quickly as possible after stowing your " \
            "carry-on items."
    message = "Please, using your microscope's UI and the microscope control panel, insert and align the required " \
              "selected area diffraction (SAD) aperture." \
              "\n\nOnce the SAD aperture is aligned, please remove it." \
              "\n\nOnce the SAD aperture has been removed, please click the continue button."
    return title, message


def get_start_message() -> Tuple[str, str]:
    """
    :return: str: A start message.
    """
    title = "Flight attendants, prepare doors for departure and cross-check."
    message = "We are now ready to perform a MicroED tilt acquisition series! Please refrain from touching the " \
              "microscope controls for the duration of the experiment. If at any point you need to stop the " \
              "experiment, please hit Ctrl-C on your keyboard. " \
              "\n\nUpon pressing continue, the stage will be removed and the automated acquisition series will begin!"
    return title, message


def get_end_message(out_file) -> Tuple[str, str]:
    """
    :param: out_file: str:
        The out file path.
    :return: str: An end message.
    """
    title = "Ladies and gentlemen, we have begun our descent into Ludwigshafen, where the weather is a balmy " \
            "30 degrees centigrade."
    message = "We have now completed the MicroED tilt acquisition series!" \
              "\n\nYour images can be found in " + str(out_file) + \
              "\n\n\u03B1 stage tilt, beam shift, and image shift will be zeroed upon script termination."
    return title, message


def get_good_bye_message() -> Tuple[str, str]:
    """
    :return: str: A good bye message.
    """
    title = "Thank you for flying with Air TEM, we hope to see you again soon!"
    message = "Thank you for using BASF's in house MicroED automated imaging script. Please report any issues on " \
              "GitHub: https://github.com/mrl280/pyTEM/issues."
    return title, message


def display_message(title: str, message: str, microscope: Union[Interface, None], position: str = "centered") -> None:
    """
    Display a simple message box with 'continue' and 'exit' buttons at the bottom.

    :param message: str:
        The message to display.
    :param title: str:
        Message box title.

    :param microscope: pyTEM Interface (or None):
        The microscope interface, needed to return the microscope to a safe state if the user exits the script
         through the quit button on the message box.

    :param position: str:
        The position of the message box, one of:
        - "centered" (useful when you need the users full attention, and don't want them fiddling around with the
                      microscope in the background)
        - "out-of-the-way" (useful when you need the user to adjust the microscope in the background before confirming)

    :return: None.
    """
    root = tk.Tk()
    style = ttk.Style()

    root.title(title)
    add_basf_icon_to_tkinter_window(root)

    window_width = 650
    message = ttk.Label(root, text=message, wraplength=window_width, font=(None, 15), justify='center')
    message.grid(column=0, columnspan=2, row=0, padx=5, pady=5)

    # Create continue and exit buttons
    continue_button = ttk.Button(root, text="Continue", command=lambda: root.destroy(), style="big.TButton")
    continue_button.grid(column=0, row=1, sticky="e", padx=5, pady=5)
    exit_button = ttk.Button(root, text="Quit", command=lambda: exit_script(microscope=microscope, status=1),
                             style="big.TButton")
    exit_button.grid(column=1, row=1, sticky="w", padx=5, pady=5)

    style.configure('big.TButton', font=(None, 10), foreground="blue4")

    if position == "centered":
        root.eval('tk::PlaceWindow . center')  # Center the window on the screen

    elif position == "out-of-the-way":
        root.geometry("{width}x{height}+{x}+{y}".format(width=window_width, height=215,
                                                        x=int(0.65 * root.winfo_screenwidth()),
                                                        y=int(0.025 * root.winfo_screenheight())))
    else:
        raise Exception("Display message position '" + str(position) + "' not recognized.")

    root.mainloop()


if __name__ == "__main__":
    """ Testing """
    title_, message_ = get_eucentric_height_message()
    display_message(title=title_, message=message_, microscope=None, position="centered")
