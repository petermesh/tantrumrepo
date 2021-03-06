# -*- coding: utf-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Complex News
# Addon id: plugin.audio.complexnews
# Addon Provider: MuadDib

#######################################################################
#Import Modules Section
import base64, os, sys, urlparse
import xbmc, xbmcaddon, xbmcplugin
#######################################################################

#######################################################################
# Primary Addon Variables 
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
THISADDON           = xbmcaddon.Addon(id=AddonID)
ADDON_ID            = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE          = base64.b64decode(b'Q29tcGxleCBOZXdz')
USER_AGENT          = base64.b64decode(b'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNDAuMC4yMjE0Ljg1IFNhZmFyaS81MzcuMzY=')
#######################################################################

#######################################################################
# Path Variables
HOMEPATH            = xbmc.translatePath('special://home/')
ADDONSPATH          = os.path.join(HOMEPATH, 'addons')
USERDATAPATH        = os.path.join(HOMEPATH, 'userdata')
ADDONDATAPATH       = xbmc.translatePath(os.path.join(USERDATAPATH, 'addon_data'))
LOGPATH             = xbmc.translatePath('special://logpath/')
THISADDONPATH       = os.path.join(ADDONSPATH, ADDON_ID)
YTADDONPATH         = os.path.join(ADDONSPATH, 'plugin.video.youtube')
YTADDONDATAPATH     = os.path.join(ADDONDATAPATH, 'plugin.video.youtube')
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvdGFudHJ1bXhtbHMvbWFzdGVyL2NvbXBsZXhuZXdzLw==')
MAINMENUFILE        = urlparse.urljoin(BASEURL, base64.b64decode(b'bWFpbi50eHQ='))
NEWSFILE            = urlparse.urljoin(BASEURL, base64.b64decode(b'bmV3cy54bWw='))
#######################################################################

#######################################################################
# Artwork Variables 
ARTFOLDER           = os.path.join(THISADDONPATH,'resources','media')
DEFAULTICON         = os.path.join(THISADDONPATH, 'icon.png')
DEFAULTFANART       = os.path.join(THISADDONPATH, 'fanart.jpg')
DEFAULTBLANK        = os.path.join(ARTFOLDER, 'pixel.png')
#######################################################################

#######################################################################
# Settings Variables 
DEBUGMODE           = THISADDON.getSetting('debug')
#######################################################################

def add_sort_methods():
    sort_methods = [xbmcplugin.SORT_METHOD_LABEL,xbmcplugin.SORT_METHOD_UNSORTED,xbmcplugin.SORT_METHOD_DATE,xbmcplugin.SORT_METHOD_DURATION,xbmcplugin.SORT_METHOD_EPISODE]
    for method in sort_methods:
        xbmcplugin.addSortMethod(int(sys.argv[1]), sortMethod=method)
    return