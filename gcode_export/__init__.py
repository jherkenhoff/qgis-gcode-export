# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GcodeExport
                                 A QGIS plugin
 Lets you export your project to G-code for usage with a pen plotter
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-08
        copyright            : (C) 2020 by mr.kenhoff
        email                : mrkenhoff+qgis@mailbox.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GcodeExport class from file GcodeExport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gcode_export import GcodeExport
    return GcodeExport(iface)
