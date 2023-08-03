{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMrP6qNQp62MmKg35ei1iXW",
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
        "<a href=\"https://colab.research.google.com/github/Nelrau/python_basic/blob/basic/funcao_titulo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sqk8lpZDwbFA",
        "outputId": "284f7d62-2321-4a62-9113-5dcb98a83f8f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "______\n",
            "Uarlen\n",
            "______\n",
            "______\n",
            "Python\n",
            "______\n"
          ]
        }
      ],
      "source": [
        "def printar(msg):\n",
        "  print('_'*len(msg))\n",
        "  print(f'{msg}')\n",
        "  print('_'*len(msg))\n",
        "\n",
        "printar('Uarlen')\n",
        "printar('Python')"
      ]
    }
  ]
}