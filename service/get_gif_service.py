import os
import requests
from bs4 import BeautifulSoup


class GetGifService:
    BASE_URL = "https://www3.worldrag.com/database/?act=mobsearch&id=&cname=on&name="
    ASSET_DIR = "assets"

    @staticmethod
    def get_gif(monstro_nome: str) -> str | None:
        nome_formatado = monstro_nome.strip().replace(" ", "+")
        gif_path = os.path.join(GetGifService.ASSET_DIR, f"{monstro_nome}.gif")

        if os.path.exists(gif_path):
            return gif_path

        try:
            url = GetGifService.BASE_URL + nome_formatado
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            img_tag = soup.select_one("td.mobimg img")
            if not img_tag:
                return None

            gif_src = img_tag.get("src")
            if not gif_src.startswith("http"):
                gif_src = "https://www3.worldrag.com/database/" + gif_src

            gif_bytes = requests.get(gif_src).content

            os.makedirs(GetGifService.ASSET_DIR, exist_ok=True)
            with open(gif_path, "wb") as f:
                f.write(gif_bytes)

            return gif_path
        except Exception as e:
            print(f"[ERRO] ao buscar gif: {e}")
            return None
