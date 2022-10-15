{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdhKetqvh30ry6w6lWBH8Z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/javocone4/Entregable1/blob/main/Simpsons.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Entregable 1."
      ],
      "metadata": {
        "id": "hRcJKjjEjrkF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import json\n",
        "import time\n",
        "\n",
        "ListGen = []\n",
        "ListaHomer = []\n",
        "ListaLisa = []\n",
        "while True :\n",
        "    URL = \"https://thesimpsonsquoteapi.glitch.me/quotes\"\n",
        "    data = requests.get(url = URL)\n",
        "    quote = data.json()\n",
        "    personaje: str = quote[0]['character']\n",
        "    frase: str = quote[0]['quote']\n",
        "    if personaje == 'Homer Simpson':\n",
        "      ListGen.append(personaje)\n",
        "      ListGen.append(frase)\n",
        "      ListaHomer.append(personaje)\n",
        "      ListaHomer.append(frase)\n",
        "    elif personaje == 'Lisa Simpson':\n",
        "      ListGen.append(personaje)\n",
        "      ListGen.append(frase)\n",
        "      ListaLisa.append(personaje)\n",
        "      ListaLisa.append(frase)\n",
        "    else:\n",
        "      ListGen.append(personaje)\n",
        "      ListGen.append(frase)\n",
        "    \n",
        "    print(frase)\n",
        "    \n",
        "    time.sleep(30)\n",
        "\n",
        "    \n",
        "    \n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 258
        },
        "id": "S18xlPUGjp19",
        "outputId": "f97e0bb7-d67d-44ec-cf44-6cf6d5ac108d"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Can't we have one meeting that doesn't end with us digging up a corpse?\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-23-26551a8a2c8f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     28\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfrase\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m     \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m30\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     31\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "mcHwLcjE3rCr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}