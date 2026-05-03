import decky_plugin
import json
import os
import shutil
from plugin_settings import merge_tdp_profiles, get_saved_settings, set_setting
import device_utils
import ryzenadj

UPSTREAM_PLUGIN_NAME = "SimpleDeckyTDP"

def migrate_from_simpledecky_tdp():
  """One-time import of settings from an existing SimpleDeckyTDP install.

  Runs only when this plugin's settings file is empty/absent and the
  upstream SimpleDeckyTDP settings file exists. Lets users carry their
  per-game profiles over to ROGAllyTDP without manual file copying.
  """
  try:
    new_dir = os.environ.get("DECKY_PLUGIN_SETTINGS_DIR")
    if not new_dir:
      return

    settings_root = os.path.dirname(new_dir)
    old_settings_path = os.path.join(settings_root, UPSTREAM_PLUGIN_NAME, "settings.json")
    new_settings_path = os.path.join(new_dir, "settings.json")

    if not os.path.exists(old_settings_path):
      return

    if os.path.exists(new_settings_path):
      try:
        with open(new_settings_path, "r") as f:
          existing = json.load(f)
        if existing:
          # User already has settings here — don't overwrite.
          return
      except Exception:
        # Malformed or empty file: fall through and import.
        pass

    os.makedirs(new_dir, exist_ok=True)
    shutil.copy2(old_settings_path, new_settings_path)
    decky_plugin.logger.info(
      f"{__name__} imported settings from {UPSTREAM_PLUGIN_NAME} "
      f"({old_settings_path} -> {new_settings_path})"
    )
  except Exception as e:
    decky_plugin.logger.error(f"{__name__} migrate_from_simpledecky_tdp error {e}")

def check_ryzenadj_coall_support(force_check=False):
  if not device_utils.is_intel():
    try:
      settings = get_saved_settings()
      if force_check or settings.get('supportsRyzenadjCoall', None) == None:
        undervolt_supported = bool(ryzenadj._set_ryzenadj_undervolt(0))

        set_setting('supportsRyzenadjCoall', undervolt_supported)
    except Exception as e:
      decky_plugin.logger.error(f"{__name__} error while checking undervolt support {e}")

# def migrate_smt():
#   try:
#     settings = get_saved_settings()
#     if not settings.get('tdpProfiles'):
#       settings['tdpProfiles'] = {}
#     tdp_profiles = settings.get('tdpProfiles')

#     for game_id in tdp_profiles:
#       profile = tdp_profiles[game_id]

#       smt = profile.get('smt', None)

#       if not isinstance(smt, bool):
#         profile['smt'] = True

#     merge_tdp_profiles(tdp_profiles)
#   except Exception as e:
#     decky_plugin.logger.error(f"{__name__} error while setting default smt values {e}")

# def migrate_gpu_mode():
#   try:
#     settings = get_saved_settings()
#     if not settings.get('tdpProfiles'):
#       settings['tdpProfiles'] = {}
#     tdp_profiles = settings.get('tdpProfiles')

#     for game_id in tdp_profiles:
#       profile = tdp_profiles[game_id]

#       mode = profile.get('gpuMode', None)

#       if mode == 'PERFORMANCE':
#         profile['gpuMode'] = 'BALANCE'

#     merge_tdp_profiles(tdp_profiles)
#   except Exception as e:
#     decky_plugin.logger.error(f"{__name__} error while setting default smt values {e}")
