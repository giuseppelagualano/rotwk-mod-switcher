# core/archiver.py
import logging
import shutil
import tempfile
from pyBIG import Archive

logger = logging.getLogger(__name__)

def create_trowmod_ini_big_archive(source_dir_path: str, output_dir_path: str, archive_name: str) -> bool:

    archive_path = output_dir_path + archive_name

    try:
        logger.info(f"Creating BIG archive from directory: {source_dir_path}")

        with tempfile.TemporaryDirectory(prefix="pybig_ini_") as temp_staging_dir_str:

            logger.debug(f"Using temporary directory for staging ini archive: {temp_staging_dir_str}")

            logger.info(f"Copying '{source_dir_path}' to '{temp_staging_dir_str}'...")
            shutil.copytree(source_dir_path + "/data", temp_staging_dir_str+"/data", dirs_exist_ok=True)
            logger.debug("Copy complete.")

            logger.info(f"Creating INI BIG archive from directory: {temp_staging_dir_str}")

            archive = Archive.from_directory(temp_staging_dir_str)

            logger.info(f"Saving archive to: {archive_path}")
            archive.save(archive_path)

            logger.info(f"Archive created successfully: {archive_path}")

        return True

    except OSError as e:
        logger.error(f"OS error during archive creation: {e}", exc_info=True)
        return False
    except Exception as e:
        logger.error(f"An unexpected error occurred during archive creation: {e}", exc_info=True)
        return False

def create_trowmod_arts_big_archive(source_dir_path: str, output_dir_path: str, archive_name: str) -> bool:

    archive_path = output_dir_path + archive_name

    try:
        logger.info(f"Creating BIG archive from directory: {source_dir_path}")

        with tempfile.TemporaryDirectory(prefix="pybig_arts_") as temp_staging_dir_str:

            logger.debug(f"Using temporary directory for staging arts archive: {temp_staging_dir_str}")

            logger.info(f"Copying '{source_dir_path}' to '{temp_staging_dir_str}'...")
            shutil.copytree(source_dir_path + "/arts", temp_staging_dir_str, dirs_exist_ok=True)
            logger.debug("Copy complete.")

            logger.info(f"Creating Arts BIG archive from directory: {temp_staging_dir_str}")

            archive = Archive.from_directory(temp_staging_dir_str)

            logger.info(f"Saving archive to: {archive_path}")
            archive.save(archive_path)

            logger.info(f"Archive created successfully: {archive_path}")

        return True

    except OSError as e:
        logger.error(f"OS error during archive creation: {e}", exc_info=True)
        return False
    except Exception as e:
        logger.error(f"An unexpected error occurred during archive creation: {e}", exc_info=True)
        return False
