import sys

from spacy.util import run_command
from wasabi import msg

WIKIGRAPHS_TABLE = {
    "enwiki_core": "https://errequadrosrl-my.sharepoint.com/:u:/g/personal/paolo_arduin_errequadrosrl_onmicrosoft_com/ESedYiVvufpCtImuOlFXm6MB_5YyfKQnZIvDinnYbL-NmA?Download=1",
    "simplewiki_core": "https://errequadrosrl-my.sharepoint.com/:u:/g/personal/paolo_arduin_errequadrosrl_onmicrosoft_com/EQhheXcD9KtGpXyoZ9a2zOEBmGIvZXuyFoV1KoYOzgsjLw?Download=1",
}


def download_wikigraph(wg_name):
    if wg_name not in WIKIGRAPHS_TABLE:
        msg.fail(
            f"{wg_name} not available yet. Try with: {', '.join(WIKIGRAPHS_TABLE)}",
            exits=1,
        )
    wg_tar = f"{wg_name}.tar.gz"
    run_command(
        f"wget {WIKIGRAPHS_TABLE[wg_name]} -O {wg_tar} &&"
        f"{sys.executable} -m pip install --no-deps --force-reinstall --no-cache {wg_tar} &&"
        f"rm {wg_tar}"
    )