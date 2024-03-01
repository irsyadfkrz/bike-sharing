{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "H9wADwK78DCz"
      },
      "source": [
        "# **Proyek Analisis Data: Bike Sharing**\n",
        "- **Nama:** Muhammad Irsyad Fikri Azhar\n",
        "- **Email:** irsyadfkrz10@gmail.com\n",
        "- **ID Dicoding:** irsyadfkrz"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eE0raob58DC0"
      },
      "source": [
        "## Menentukan Pertanyaan Bisnis"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GmQeQ5YF8DC0"
      },
      "source": [
        "- Bagaimana pola penggunaan penyewaan sepeda pada hari kerja dibandingkan dengan hari libur?\n",
        "- Apakah penggunaan meningkat saat cuaca cerah atau menurun saat hujan?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "H-z4QGlO8DC1"
      },
      "source": [
        "## Import Semua Packages/Library yang Digunakan"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 750,
      "metadata": {
        "id": "FVYwaObI8DC1"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h_Sh51Xy8DC1"
      },
      "source": [
        "## Data Wrangling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sXU2GBYu8DC1"
      },
      "source": [
        "### Gathering Data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 615,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "zjCBk1BI8DC1",
        "outputId": "1e8f3cab-cf6a-4bb2-f80b-6335805a2418"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>0.160446</td>\n",
              "      <td>331</td>\n",
              "      <td>654</td>\n",
              "      <td>985</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-02</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>0.248539</td>\n",
              "      <td>131</td>\n",
              "      <td>670</td>\n",
              "      <td>801</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-03</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>0.248309</td>\n",
              "      <td>120</td>\n",
              "      <td>1229</td>\n",
              "      <td>1349</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-04</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>0.160296</td>\n",
              "      <td>108</td>\n",
              "      <td>1454</td>\n",
              "      <td>1562</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-05</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>0.186900</td>\n",
              "      <td>82</td>\n",
              "      <td>1518</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant      dteday  season  yr  mnth  holiday  weekday  workingday  \\\n",
              "0        1  2011-01-01       1   0     1        0        6           0   \n",
              "1        2  2011-01-02       1   0     1        0        0           0   \n",
              "2        3  2011-01-03       1   0     1        0        1           1   \n",
              "3        4  2011-01-04       1   0     1        0        2           1   \n",
              "4        5  2011-01-05       1   0     1        0        3           1   \n",
              "\n",
              "   weathersit      temp     atemp       hum  windspeed  casual  registered  \\\n",
              "0           2  0.344167  0.363625  0.805833   0.160446     331         654   \n",
              "1           2  0.363478  0.353739  0.696087   0.248539     131         670   \n",
              "2           1  0.196364  0.189405  0.437273   0.248309     120        1229   \n",
              "3           1  0.200000  0.212122  0.590435   0.160296     108        1454   \n",
              "4           1  0.226957  0.229270  0.436957   0.186900      82        1518   \n",
              "\n",
              "    cnt  \n",
              "0   985  \n",
              "1   801  \n",
              "2  1349  \n",
              "3  1562  \n",
              "4  1600  "
            ]
          },
          "execution_count": 615,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df = pd.read_csv(\"data/day.csv\")\n",
        "day_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 616,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "V-ph39-iOYO0",
        "outputId": "254c9e35-dc0a-4771-b1e9-23e7c23c35e3"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>hr</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.81</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>8</td>\n",
              "      <td>32</td>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>27</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>10</td>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant      dteday  season  yr  mnth  hr  holiday  weekday  workingday  \\\n",
              "0        1  2011-01-01       1   0     1   0        0        6           0   \n",
              "1        2  2011-01-01       1   0     1   1        0        6           0   \n",
              "2        3  2011-01-01       1   0     1   2        0        6           0   \n",
              "3        4  2011-01-01       1   0     1   3        0        6           0   \n",
              "4        5  2011-01-01       1   0     1   4        0        6           0   \n",
              "\n",
              "   weathersit  temp   atemp   hum  windspeed  casual  registered  cnt  \n",
              "0           1  0.24  0.2879  0.81        0.0       3          13   16  \n",
              "1           1  0.22  0.2727  0.80        0.0       8          32   40  \n",
              "2           1  0.22  0.2727  0.80        0.0       5          27   32  \n",
              "3           1  0.24  0.2879  0.75        0.0       3          10   13  \n",
              "4           1  0.24  0.2879  0.75        0.0       0           1    1  "
            ]
          },
          "execution_count": 616,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df = pd.read_csv(\"data/hour.csv\")\n",
        "hour_df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FHSiqaZp8DC1"
      },
      "source": [
        "### Assessing Data"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ic0O0e2MThrk"
      },
      "source": [
        "#### Assesing day_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 617,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ax-3tEjc9Cj1",
        "outputId": "2745a903-799a-4659-fd61-b32535671ea5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 731 entries, 0 to 730\n",
            "Data columns (total 16 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   instant     731 non-null    int64  \n",
            " 1   dteday      731 non-null    object \n",
            " 2   season      731 non-null    int64  \n",
            " 3   yr          731 non-null    int64  \n",
            " 4   mnth        731 non-null    int64  \n",
            " 5   holiday     731 non-null    int64  \n",
            " 6   weekday     731 non-null    int64  \n",
            " 7   workingday  731 non-null    int64  \n",
            " 8   weathersit  731 non-null    int64  \n",
            " 9   temp        731 non-null    float64\n",
            " 10  atemp       731 non-null    float64\n",
            " 11  hum         731 non-null    float64\n",
            " 12  windspeed   731 non-null    float64\n",
            " 13  casual      731 non-null    int64  \n",
            " 14  registered  731 non-null    int64  \n",
            " 15  cnt         731 non-null    int64  \n",
            "dtypes: float64(4), int64(11), object(1)\n",
            "memory usage: 91.5+ KB\n"
          ]
        }
      ],
      "source": [
        "day_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 618,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Muovg-SKP8OI",
        "outputId": "f4d29952-ad51-46fc-fd40-18de5e7367bd"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "instant       0\n",
              "dteday        0\n",
              "season        0\n",
              "yr            0\n",
              "mnth          0\n",
              "holiday       0\n",
              "weekday       0\n",
              "workingday    0\n",
              "weathersit    0\n",
              "temp          0\n",
              "atemp         0\n",
              "hum           0\n",
              "windspeed     0\n",
              "casual        0\n",
              "registered    0\n",
              "cnt           0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 618,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 619,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7r8H7mnYPZ1p",
        "outputId": "72aef444-6e6d-40cd-f077-a02ddd3070d8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "instant                int64\n",
            "dteday        datetime64[ns]\n",
            "season                 int64\n",
            "yr                     int64\n",
            "mnth                   int64\n",
            "holiday                int64\n",
            "weekday                int64\n",
            "workingday             int64\n",
            "weathersit             int64\n",
            "temp                 float64\n",
            "atemp                float64\n",
            "hum                  float64\n",
            "windspeed            float64\n",
            "casual                 int64\n",
            "registered             int64\n",
            "cnt                    int64\n",
            "dtype: object\n"
          ]
        }
      ],
      "source": [
        "# Mengubah Tipe data Dteday menjadi Datetime pada Day_df\n",
        "day_df['dteday'] = pd.to_datetime(day_df['dteday'], format='%Y-%m-%d')\n",
        "print(day_df.dtypes)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 620,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gnkd7v5nQMp3",
        "outputId": "29055c06-db7a-4555-a30c-6dad1569d278"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Jumlah duplikasi:  0\n"
          ]
        }
      ],
      "source": [
        "print(\"Jumlah duplikasi: \", day_df.duplicated().sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 621,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "gOc7bAdqQeJr",
        "outputId": "9bf19f84-b7c2-4f59-9602-92357a50b1fd"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>366.000000</td>\n",
              "      <td>2.496580</td>\n",
              "      <td>0.500684</td>\n",
              "      <td>6.519836</td>\n",
              "      <td>0.028728</td>\n",
              "      <td>2.997264</td>\n",
              "      <td>0.683995</td>\n",
              "      <td>1.395349</td>\n",
              "      <td>0.495385</td>\n",
              "      <td>0.474354</td>\n",
              "      <td>0.627894</td>\n",
              "      <td>0.190486</td>\n",
              "      <td>848.176471</td>\n",
              "      <td>3656.172367</td>\n",
              "      <td>4504.348837</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>211.165812</td>\n",
              "      <td>1.110807</td>\n",
              "      <td>0.500342</td>\n",
              "      <td>3.451913</td>\n",
              "      <td>0.167155</td>\n",
              "      <td>2.004787</td>\n",
              "      <td>0.465233</td>\n",
              "      <td>0.544894</td>\n",
              "      <td>0.183051</td>\n",
              "      <td>0.162961</td>\n",
              "      <td>0.142429</td>\n",
              "      <td>0.077498</td>\n",
              "      <td>686.622488</td>\n",
              "      <td>1560.256377</td>\n",
              "      <td>1937.211452</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.059130</td>\n",
              "      <td>0.079070</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.022392</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>22.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>183.500000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.337083</td>\n",
              "      <td>0.337842</td>\n",
              "      <td>0.520000</td>\n",
              "      <td>0.134950</td>\n",
              "      <td>315.500000</td>\n",
              "      <td>2497.000000</td>\n",
              "      <td>3152.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>366.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.498333</td>\n",
              "      <td>0.486733</td>\n",
              "      <td>0.626667</td>\n",
              "      <td>0.180975</td>\n",
              "      <td>713.000000</td>\n",
              "      <td>3662.000000</td>\n",
              "      <td>4548.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>548.500000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.655417</td>\n",
              "      <td>0.608602</td>\n",
              "      <td>0.730209</td>\n",
              "      <td>0.233214</td>\n",
              "      <td>1096.000000</td>\n",
              "      <td>4776.500000</td>\n",
              "      <td>5956.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>731.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.861667</td>\n",
              "      <td>0.840896</td>\n",
              "      <td>0.972500</td>\n",
              "      <td>0.507463</td>\n",
              "      <td>3410.000000</td>\n",
              "      <td>6946.000000</td>\n",
              "      <td>8714.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          instant      season          yr        mnth     holiday     weekday  \\\n",
              "count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   \n",
              "mean   366.000000    2.496580    0.500684    6.519836    0.028728    2.997264   \n",
              "std    211.165812    1.110807    0.500342    3.451913    0.167155    2.004787   \n",
              "min      1.000000    1.000000    0.000000    1.000000    0.000000    0.000000   \n",
              "25%    183.500000    2.000000    0.000000    4.000000    0.000000    1.000000   \n",
              "50%    366.000000    3.000000    1.000000    7.000000    0.000000    3.000000   \n",
              "75%    548.500000    3.000000    1.000000   10.000000    0.000000    5.000000   \n",
              "max    731.000000    4.000000    1.000000   12.000000    1.000000    6.000000   \n",
              "\n",
              "       workingday  weathersit        temp       atemp         hum   windspeed  \\\n",
              "count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   \n",
              "mean     0.683995    1.395349    0.495385    0.474354    0.627894    0.190486   \n",
              "std      0.465233    0.544894    0.183051    0.162961    0.142429    0.077498   \n",
              "min      0.000000    1.000000    0.059130    0.079070    0.000000    0.022392   \n",
              "25%      0.000000    1.000000    0.337083    0.337842    0.520000    0.134950   \n",
              "50%      1.000000    1.000000    0.498333    0.486733    0.626667    0.180975   \n",
              "75%      1.000000    2.000000    0.655417    0.608602    0.730209    0.233214   \n",
              "max      1.000000    3.000000    0.861667    0.840896    0.972500    0.507463   \n",
              "\n",
              "            casual   registered          cnt  \n",
              "count   731.000000   731.000000   731.000000  \n",
              "mean    848.176471  3656.172367  4504.348837  \n",
              "std     686.622488  1560.256377  1937.211452  \n",
              "min       2.000000    20.000000    22.000000  \n",
              "25%     315.500000  2497.000000  3152.000000  \n",
              "50%     713.000000  3662.000000  4548.000000  \n",
              "75%    1096.000000  4776.500000  5956.000000  \n",
              "max    3410.000000  6946.000000  8714.000000  "
            ]
          },
          "execution_count": 621,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 622,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A0b2huu0bH-N",
        "outputId": "c4cb4af7-2f63-4d16-fbcb-826ccfe3bbc3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "yr              2\n",
              "holiday         2\n",
              "workingday      2\n",
              "weathersit      3\n",
              "season          4\n",
              "weekday         7\n",
              "mnth           12\n",
              "temp          499\n",
              "hum           595\n",
              "casual        606\n",
              "windspeed     650\n",
              "registered    679\n",
              "atemp         690\n",
              "cnt           696\n",
              "instant       731\n",
              "dteday        731\n",
              "dtype: int64"
            ]
          },
          "execution_count": 622,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Memeriksa jumlah baris unik dalam setiap fitur\n",
        "day_df.nunique().sort_values()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d8pUUZxJQRUv"
      },
      "source": [
        "#### Assesing Hour_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 623,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pB3mS3ZEPM7U",
        "outputId": "fc917909-5987-463f-f98b-c1ba30ac5b3b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17379 entries, 0 to 17378\n",
            "Data columns (total 17 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   instant     17379 non-null  int64  \n",
            " 1   dteday      17379 non-null  object \n",
            " 2   season      17379 non-null  int64  \n",
            " 3   yr          17379 non-null  int64  \n",
            " 4   mnth        17379 non-null  int64  \n",
            " 5   hr          17379 non-null  int64  \n",
            " 6   holiday     17379 non-null  int64  \n",
            " 7   weekday     17379 non-null  int64  \n",
            " 8   workingday  17379 non-null  int64  \n",
            " 9   weathersit  17379 non-null  int64  \n",
            " 10  temp        17379 non-null  float64\n",
            " 11  atemp       17379 non-null  float64\n",
            " 12  hum         17379 non-null  float64\n",
            " 13  windspeed   17379 non-null  float64\n",
            " 14  casual      17379 non-null  int64  \n",
            " 15  registered  17379 non-null  int64  \n",
            " 16  cnt         17379 non-null  int64  \n",
            "dtypes: float64(4), int64(12), object(1)\n",
            "memory usage: 2.3+ MB\n"
          ]
        }
      ],
      "source": [
        "hour_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 624,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9WBx9NhjPaGN",
        "outputId": "1b60aedf-ecdf-45e2-d2f9-93ef2cf45505"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Jumlah duplikasi:  0\n"
          ]
        }
      ],
      "source": [
        "print(\"Jumlah duplikasi: \", hour_df.duplicated().sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 625,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EMP77MFAPaBx",
        "outputId": "54e10646-6fd1-4e01-8652-3e4364aa235c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "instant       0\n",
              "dteday        0\n",
              "season        0\n",
              "yr            0\n",
              "mnth          0\n",
              "hr            0\n",
              "holiday       0\n",
              "weekday       0\n",
              "workingday    0\n",
              "weathersit    0\n",
              "temp          0\n",
              "atemp         0\n",
              "hum           0\n",
              "windspeed     0\n",
              "casual        0\n",
              "registered    0\n",
              "cnt           0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 625,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 626,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "isBy_fzGPaJk",
        "outputId": "90941ee4-aa6c-4d6a-f0cd-30eed8a38eea"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>hr</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>2.501640</td>\n",
              "      <td>0.502561</td>\n",
              "      <td>6.537775</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.028770</td>\n",
              "      <td>3.003683</td>\n",
              "      <td>0.682721</td>\n",
              "      <td>1.425283</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>35.676218</td>\n",
              "      <td>153.786869</td>\n",
              "      <td>189.463088</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5017.0295</td>\n",
              "      <td>1.106918</td>\n",
              "      <td>0.500008</td>\n",
              "      <td>3.438776</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.167165</td>\n",
              "      <td>2.005771</td>\n",
              "      <td>0.465431</td>\n",
              "      <td>0.639357</td>\n",
              "      <td>0.192556</td>\n",
              "      <td>0.171850</td>\n",
              "      <td>0.192930</td>\n",
              "      <td>0.122340</td>\n",
              "      <td>49.305030</td>\n",
              "      <td>151.357286</td>\n",
              "      <td>181.387599</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.020000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>4345.5000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.333300</td>\n",
              "      <td>0.480000</td>\n",
              "      <td>0.104500</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>40.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.484800</td>\n",
              "      <td>0.630000</td>\n",
              "      <td>0.194000</td>\n",
              "      <td>17.000000</td>\n",
              "      <td>115.000000</td>\n",
              "      <td>142.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>13034.5000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.660000</td>\n",
              "      <td>0.621200</td>\n",
              "      <td>0.780000</td>\n",
              "      <td>0.253700</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>220.000000</td>\n",
              "      <td>281.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.850700</td>\n",
              "      <td>367.000000</td>\n",
              "      <td>886.000000</td>\n",
              "      <td>977.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          instant        season            yr          mnth            hr  \\\n",
              "count  17379.0000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean    8690.0000      2.501640      0.502561      6.537775     11.546752   \n",
              "std     5017.0295      1.106918      0.500008      3.438776      6.914405   \n",
              "min        1.0000      1.000000      0.000000      1.000000      0.000000   \n",
              "25%     4345.5000      2.000000      0.000000      4.000000      6.000000   \n",
              "50%     8690.0000      3.000000      1.000000      7.000000     12.000000   \n",
              "75%    13034.5000      3.000000      1.000000     10.000000     18.000000   \n",
              "max    17379.0000      4.000000      1.000000     12.000000     23.000000   \n",
              "\n",
              "            holiday       weekday    workingday    weathersit          temp  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.028770      3.003683      0.682721      1.425283      0.496987   \n",
              "std        0.167165      2.005771      0.465431      0.639357      0.192556   \n",
              "min        0.000000      0.000000      0.000000      1.000000      0.020000   \n",
              "25%        0.000000      1.000000      0.000000      1.000000      0.340000   \n",
              "50%        0.000000      3.000000      1.000000      1.000000      0.500000   \n",
              "75%        0.000000      5.000000      1.000000      2.000000      0.660000   \n",
              "max        1.000000      6.000000      1.000000      4.000000      1.000000   \n",
              "\n",
              "              atemp           hum     windspeed        casual    registered  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.475775      0.627229      0.190098     35.676218    153.786869   \n",
              "std        0.171850      0.192930      0.122340     49.305030    151.357286   \n",
              "min        0.000000      0.000000      0.000000      0.000000      0.000000   \n",
              "25%        0.333300      0.480000      0.104500      4.000000     34.000000   \n",
              "50%        0.484800      0.630000      0.194000     17.000000    115.000000   \n",
              "75%        0.621200      0.780000      0.253700     48.000000    220.000000   \n",
              "max        1.000000      1.000000      0.850700    367.000000    886.000000   \n",
              "\n",
              "                cnt  \n",
              "count  17379.000000  \n",
              "mean     189.463088  \n",
              "std      181.387599  \n",
              "min        1.000000  \n",
              "25%       40.000000  \n",
              "50%      142.000000  \n",
              "75%      281.000000  \n",
              "max      977.000000  "
            ]
          },
          "execution_count": 626,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 627,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Z73b_KzbMk_",
        "outputId": "a33cb4e0-f08a-4fb7-84d0-5f327e8effb4"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "workingday        2\n",
              "yr                2\n",
              "holiday           2\n",
              "season            4\n",
              "weathersit        4\n",
              "weekday           7\n",
              "mnth             12\n",
              "hr               24\n",
              "windspeed        30\n",
              "temp             50\n",
              "atemp            65\n",
              "hum              89\n",
              "casual          322\n",
              "dteday          731\n",
              "registered      776\n",
              "cnt             869\n",
              "instant       17379\n",
              "dtype: int64"
            ]
          },
          "execution_count": 627,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Memeriksa jumlah baris unik dalam setiap fitur\n",
        "hour_df.nunique().sort_values()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EhN5R4hr8DC1"
      },
      "source": [
        "### Cleaning Data"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "u7Wi_2qnUiCh"
      },
      "source": [
        "#### Cleaning Day_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 628,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jVnYpprE9Evz",
        "outputId": "eb0386a7-d8e4-4ec1-be8e-8fabb7ef1297"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "instant                int64\n",
            "dteday        datetime64[ns]\n",
            "season                 int64\n",
            "yr                     int64\n",
            "mnth                   int64\n",
            "holiday                int64\n",
            "weekday                int64\n",
            "workingday             int64\n",
            "weathersit             int64\n",
            "temp                 float64\n",
            "atemp                float64\n",
            "hum                  float64\n",
            "windspeed            float64\n",
            "casual                 int64\n",
            "registered             int64\n",
            "cnt                    int64\n",
            "dtype: object\n"
          ]
        }
      ],
      "source": [
        "# Mengubah Tipe data Dteday menjadi Datetime pada Day_df\n",
        "day_df['dteday'] = pd.to_datetime(day_df['dteday'], format='%Y-%m-%d')\n",
        "print(day_df.dtypes)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 629,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Kp3uDzNZeXp",
        "outputId": "c1eb2ec2-a3fa-4e9d-e57a-10158c1502c8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 731 entries, 0 to 730\n",
            "Data columns (total 16 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   instant     731 non-null    int64         \n",
            " 1   dteday      731 non-null    datetime64[ns]\n",
            " 2   season      731 non-null    int64         \n",
            " 3   yr          731 non-null    int64         \n",
            " 4   mnth        731 non-null    int64         \n",
            " 5   holiday     731 non-null    int64         \n",
            " 6   weekday     731 non-null    int64         \n",
            " 7   workingday  731 non-null    int64         \n",
            " 8   weathersit  731 non-null    int64         \n",
            " 9   temp        731 non-null    float64       \n",
            " 10  atemp       731 non-null    float64       \n",
            " 11  hum         731 non-null    float64       \n",
            " 12  windspeed   731 non-null    float64       \n",
            " 13  casual      731 non-null    int64         \n",
            " 14  registered  731 non-null    int64         \n",
            " 15  cnt         731 non-null    int64         \n",
            "dtypes: datetime64[ns](1), float64(4), int64(11)\n",
            "memory usage: 91.5 KB\n"
          ]
        }
      ],
      "source": [
        "day_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 630,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "5lQUhUocc5vK",
        "outputId": "6482fd39-88be-43df-b8a9-8a7a470cb1d5"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>0.160446</td>\n",
              "      <td>331</td>\n",
              "      <td>654</td>\n",
              "      <td>985</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-02</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>0.248539</td>\n",
              "      <td>131</td>\n",
              "      <td>670</td>\n",
              "      <td>801</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-03</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>0.248309</td>\n",
              "      <td>120</td>\n",
              "      <td>1229</td>\n",
              "      <td>1349</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-04</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>0.160296</td>\n",
              "      <td>108</td>\n",
              "      <td>1454</td>\n",
              "      <td>1562</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-05</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>0.186900</td>\n",
              "      <td>82</td>\n",
              "      <td>1518</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant     dteday  season  year  month  holiday  weekday  workingday  \\\n",
              "0        1 2011-01-01       1     0      1        0        6           0   \n",
              "1        2 2011-01-02       1     0      1        0        0           0   \n",
              "2        3 2011-01-03       1     0      1        0        1           1   \n",
              "3        4 2011-01-04       1     0      1        0        2           1   \n",
              "4        5 2011-01-05       1     0      1        0        3           1   \n",
              "\n",
              "   weathersit      temp     atemp       hum  windspeed  casual  registered  \\\n",
              "0           2  0.344167  0.363625  0.805833   0.160446     331         654   \n",
              "1           2  0.363478  0.353739  0.696087   0.248539     131         670   \n",
              "2           1  0.196364  0.189405  0.437273   0.248309     120        1229   \n",
              "3           1  0.200000  0.212122  0.590435   0.160296     108        1454   \n",
              "4           1  0.226957  0.229270  0.436957   0.186900      82        1518   \n",
              "\n",
              "   counts  \n",
              "0     985  \n",
              "1     801  \n",
              "2    1349  \n",
              "3    1562  \n",
              "4    1600  "
            ]
          },
          "execution_count": 630,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Mengubah nama kolom agar mudah dibaca\n",
        "day_df = day_df.rename(columns={'yr':'year', 'mnth':'month', 'cnt': 'counts'})\n",
        "day_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 631,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "VM9d5dmwYSCy",
        "outputId": "3cca1058-0efa-4675-c6e1-df4d2992b618"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<style  type=\"text/css\" >\n",
              "</style><table id=\"T_77aae89c_d7b0_11ee_8cbf_00155d34d00e\" ><thead>    <tr>        <th class=\"blank level0\" ></th>        <th class=\"col_heading level0 col0\" >instant</th>        <th class=\"col_heading level0 col1\" >dteday</th>        <th class=\"col_heading level0 col2\" >season</th>        <th class=\"col_heading level0 col3\" >year</th>        <th class=\"col_heading level0 col4\" >month</th>        <th class=\"col_heading level0 col5\" >holiday</th>        <th class=\"col_heading level0 col6\" >weekday</th>        <th class=\"col_heading level0 col7\" >workingday</th>        <th class=\"col_heading level0 col8\" >weathersit</th>        <th class=\"col_heading level0 col9\" >temp</th>        <th class=\"col_heading level0 col10\" >atemp</th>        <th class=\"col_heading level0 col11\" >hum</th>        <th class=\"col_heading level0 col12\" >windspeed</th>        <th class=\"col_heading level0 col13\" >casual</th>        <th class=\"col_heading level0 col14\" >registered</th>        <th class=\"col_heading level0 col15\" >counts</th>    </tr></thead><tbody>\n",
              "        </tbody></table>"
            ],
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x2248fa43e10>"
            ]
          },
          "execution_count": 631,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Q1 = day_df['counts'].quantile(0.25)\n",
        "Q3 = day_df['counts'].quantile(0.75)\n",
        "IQR = Q3 - Q1\n",
        "\n",
        "# Menentukan batas outlier\n",
        "lower_bound = Q1 - 1.5 * IQR\n",
        "upper_bound = Q3 + 1.5 * IQR\n",
        "\n",
        "# Identifikasi outliers\n",
        "outliers = day_df[(day_df['counts'] < lower_bound) | (day_df['counts'] > upper_bound)]\n",
        "outliers.style.background_gradient(cmap='Greys')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TMLVSSO-dsNH"
      },
      "source": [
        "##### Season (Musim)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 632,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lNjBDvTZdKTH",
        "outputId": "6f2ec70b-2a07-4b92-8a27-308519657896"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3    188\n",
            "2    184\n",
            "1    181\n",
            "4    178\n",
            "Name: season, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(day_df.season.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 633,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PC0cyB43dfOa",
        "outputId": "14f3c31f-f054-4f23-f2da-fda042060dc7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "fall      188\n",
              "summer    184\n",
              "spring    181\n",
              "winter    178\n",
              "Name: season, dtype: int64"
            ]
          },
          "execution_count": 633,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Mengubah angka 1,2,3,4 agar mudah dibaca\n",
        "day_df.season = day_df.season.map({1:'spring', 2:'summer', 3:'fall', 4:'winter'})\n",
        "day_df.season.value_counts()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X6imG1xVdz7U"
      },
      "source": [
        "##### Year (Tahun)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 634,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yemEeFped2b_",
        "outputId": "cb415a4a-ba17-4ce6-8f18-1e02c50c437a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1    366\n",
            "0    365\n",
            "Name: year, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print( day_df.year.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 635,
      "metadata": {
        "id": "IsR74Swcd9S0"
      },
      "outputs": [],
      "source": [
        "# Mengubah nama kolom agar mudah dibaca\n",
        "day_df.year = day_df.year.map({0:'2011', 1:'2012'})\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cnZqej1jeeA3"
      },
      "source": [
        "##### Month (Bulan)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 636,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QlzNQluxelEh",
        "outputId": "b0518725-9e10-48b9-ffdc-f59feb8d8677"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "12    62\n",
            "10    62\n",
            "8     62\n",
            "7     62\n",
            "5     62\n",
            "3     62\n",
            "1     62\n",
            "11    60\n",
            "9     60\n",
            "6     60\n",
            "4     60\n",
            "2     57\n",
            "Name: month, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(day_df.month.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 637,
      "metadata": {
        "id": "qjqoSxAVeqOO"
      },
      "outputs": [],
      "source": [
        "day_df.month = day_df.month.map({1:'Jan', 2:'Feb', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "igWnp408baWh"
      },
      "source": [
        "##### Weathersit (Kondisi Cuaca)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 638,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fSBaQF5xe51P",
        "outputId": "fae18cbd-baca-4c90-d140-69eb3d77ff4f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1    463\n",
            "2    247\n",
            "3     21\n",
            "Name: weathersit, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(day_df.weathersit.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 639,
      "metadata": {
        "id": "kcZa_iMNe1C3"
      },
      "outputs": [],
      "source": [
        "day_df.weathersit = day_df.weathersit.map({1:'Clear', 2:'Cloudy', 3:'Snow/Rain'})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "732DUx93bl4Y"
      },
      "source": [
        "##### Weekday"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 640,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X2Fw5hPgfl3Y",
        "outputId": "3ec6c740-c28d-4344-9f52-fdad0e0cb740"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "6    105\n",
            "1    105\n",
            "0    105\n",
            "5    104\n",
            "4    104\n",
            "3    104\n",
            "2    104\n",
            "Name: weekday, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(day_df.weekday.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 641,
      "metadata": {
        "id": "x50_Dzj8fomG"
      },
      "outputs": [],
      "source": [
        "day_df.weekday = day_df.weekday.map({0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 642,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FJbHPJtAb3Im",
        "outputId": "8a234dec-4526-46f3-93a6-f2fa72aff690"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1    500\n",
            "0    231\n",
            "Name: workingday, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(day_df.workingday.value_counts())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 643,
      "metadata": {
        "id": "76ucU4VAb8y4"
      },
      "outputs": [],
      "source": [
        "day_df.workingday = day_df.workingday.map({0:'Hari Kerja', 1:'Hari Libur',})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 644,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "qHYFY1oBgql3",
        "outputId": "c7ff49b9-015d-4a90-b1a0-efa4d6330a0d"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Sunday</td>\n",
              "      <td>Hari Kerja</td>\n",
              "      <td>Cloudy</td>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>0.160446</td>\n",
              "      <td>331</td>\n",
              "      <td>654</td>\n",
              "      <td>985</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-02</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Monday</td>\n",
              "      <td>Hari Kerja</td>\n",
              "      <td>Cloudy</td>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>0.248539</td>\n",
              "      <td>131</td>\n",
              "      <td>670</td>\n",
              "      <td>801</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-03</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Tuesday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>0.248309</td>\n",
              "      <td>120</td>\n",
              "      <td>1229</td>\n",
              "      <td>1349</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-04</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Wednesday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>0.160296</td>\n",
              "      <td>108</td>\n",
              "      <td>1454</td>\n",
              "      <td>1562</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-05</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Thursday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>0.186900</td>\n",
              "      <td>82</td>\n",
              "      <td>1518</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant     dteday  season  year month  holiday    weekday  workingday  \\\n",
              "0        1 2011-01-01  spring  2011   Jan        0     Sunday  Hari Kerja   \n",
              "1        2 2011-01-02  spring  2011   Jan        0     Monday  Hari Kerja   \n",
              "2        3 2011-01-03  spring  2011   Jan        0    Tuesday  Hari Libur   \n",
              "3        4 2011-01-04  spring  2011   Jan        0  Wednesday  Hari Libur   \n",
              "4        5 2011-01-05  spring  2011   Jan        0   Thursday  Hari Libur   \n",
              "\n",
              "  weathersit      temp     atemp       hum  windspeed  casual  registered  \\\n",
              "0     Cloudy  0.344167  0.363625  0.805833   0.160446     331         654   \n",
              "1     Cloudy  0.363478  0.353739  0.696087   0.248539     131         670   \n",
              "2      Clear  0.196364  0.189405  0.437273   0.248309     120        1229   \n",
              "3      Clear  0.200000  0.212122  0.590435   0.160296     108        1454   \n",
              "4      Clear  0.226957  0.229270  0.436957   0.186900      82        1518   \n",
              "\n",
              "   counts  \n",
              "0     985  \n",
              "1     801  \n",
              "2    1349  \n",
              "3    1562  \n",
              "4    1600  "
            ]
          },
          "execution_count": 644,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CRUV3OZ2U2Gc"
      },
      "source": [
        "#### Cleaning Hour_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 645,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1a8-LwazU5OS",
        "outputId": "a82794e2-b3c1-42fd-adee-bd12fe503163"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "instant                int64\n",
            "dteday        datetime64[ns]\n",
            "season                 int64\n",
            "yr                     int64\n",
            "mnth                   int64\n",
            "hr                     int64\n",
            "holiday                int64\n",
            "weekday                int64\n",
            "workingday             int64\n",
            "weathersit             int64\n",
            "temp                 float64\n",
            "atemp                float64\n",
            "hum                  float64\n",
            "windspeed            float64\n",
            "casual                 int64\n",
            "registered             int64\n",
            "cnt                    int64\n",
            "dtype: object\n"
          ]
        }
      ],
      "source": [
        "# Mengubah Tipe data Dteday menjadi Datetime pada Day_df\n",
        "hour_df['dteday'] = pd.to_datetime(hour_df['dteday'], format='%Y-%m-%d')\n",
        "print(hour_df.dtypes)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 646,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "16    730\n",
              "17    730\n",
              "15    729\n",
              "13    729\n",
              "14    729\n",
              "22    728\n",
              "18    728\n",
              "19    728\n",
              "20    728\n",
              "21    728\n",
              "23    728\n",
              "12    728\n",
              "7     727\n",
              "8     727\n",
              "9     727\n",
              "10    727\n",
              "11    727\n",
              "0     726\n",
              "6     725\n",
              "1     724\n",
              "5     717\n",
              "2     715\n",
              "4     697\n",
              "3     697\n",
              "Name: hr, dtype: int64"
            ]
          },
          "execution_count": 646,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df['hr'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 647,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.81</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>8</td>\n",
              "      <td>32</td>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>27</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>10</td>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant     dteday  season  year  month  hour  holiday  weekday  \\\n",
              "0        1 2011-01-01       1     0      1     0        0        6   \n",
              "1        2 2011-01-01       1     0      1     1        0        6   \n",
              "2        3 2011-01-01       1     0      1     2        0        6   \n",
              "3        4 2011-01-01       1     0      1     3        0        6   \n",
              "4        5 2011-01-01       1     0      1     4        0        6   \n",
              "\n",
              "   workingday  weathersit  temp   atemp   hum  windspeed  casual  registered  \\\n",
              "0           0           1  0.24  0.2879  0.81        0.0       3          13   \n",
              "1           0           1  0.22  0.2727  0.80        0.0       8          32   \n",
              "2           0           1  0.22  0.2727  0.80        0.0       5          27   \n",
              "3           0           1  0.24  0.2879  0.75        0.0       3          10   \n",
              "4           0           1  0.24  0.2879  0.75        0.0       0           1   \n",
              "\n",
              "   counts  \n",
              "0      16  \n",
              "1      40  \n",
              "2      32  \n",
              "3      13  \n",
              "4       1  "
            ]
          },
          "execution_count": 647,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Mengubah nama kolom agar mudah dibaca\n",
        "hour_df = hour_df.rename(columns={'yr':'year', 'mnth':'month', 'cnt': 'counts', 'hr':'hour'})\n",
        "hour_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 648,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "v0xzA2d6XVJJ",
        "outputId": "3fa1ba4e-1496-418d-b4b4-453a8e03e9f8"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.81</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>8</td>\n",
              "      <td>32</td>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>27</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>10</td>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant     dteday  season  year  month  hour  holiday  weekday  \\\n",
              "0        1 2011-01-01       1     0      1     0        0        6   \n",
              "1        2 2011-01-01       1     0      1     1        0        6   \n",
              "2        3 2011-01-01       1     0      1     2        0        6   \n",
              "3        4 2011-01-01       1     0      1     3        0        6   \n",
              "4        5 2011-01-01       1     0      1     4        0        6   \n",
              "\n",
              "   workingday  weathersit  temp   atemp   hum  windspeed  casual  registered  \\\n",
              "0           0           1  0.24  0.2879  0.81        0.0       3          13   \n",
              "1           0           1  0.22  0.2727  0.80        0.0       8          32   \n",
              "2           0           1  0.22  0.2727  0.80        0.0       5          27   \n",
              "3           0           1  0.24  0.2879  0.75        0.0       3          10   \n",
              "4           0           1  0.24  0.2879  0.75        0.0       0           1   \n",
              "\n",
              "   counts  \n",
              "0      16  \n",
              "1      40  \n",
              "2      32  \n",
              "3      13  \n",
              "4       1  "
            ]
          },
          "execution_count": 648,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 649,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mdURb4-HXcZq",
        "outputId": "03c9da3e-de2a-4a75-9ac8-a32873ac0a48"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17379 entries, 0 to 17378\n",
            "Data columns (total 17 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   instant     17379 non-null  int64         \n",
            " 1   dteday      17379 non-null  datetime64[ns]\n",
            " 2   season      17379 non-null  int64         \n",
            " 3   year        17379 non-null  int64         \n",
            " 4   month       17379 non-null  int64         \n",
            " 5   hour        17379 non-null  int64         \n",
            " 6   holiday     17379 non-null  int64         \n",
            " 7   weekday     17379 non-null  int64         \n",
            " 8   workingday  17379 non-null  int64         \n",
            " 9   weathersit  17379 non-null  int64         \n",
            " 10  temp        17379 non-null  float64       \n",
            " 11  atemp       17379 non-null  float64       \n",
            " 12  hum         17379 non-null  float64       \n",
            " 13  windspeed   17379 non-null  float64       \n",
            " 14  casual      17379 non-null  int64         \n",
            " 15  registered  17379 non-null  int64         \n",
            " 16  counts      17379 non-null  int64         \n",
            "dtypes: datetime64[ns](1), float64(4), int64(12)\n",
            "memory usage: 2.3 MB\n"
          ]
        }
      ],
      "source": [
        "hour_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 650,
      "metadata": {
        "id": "8kCKtvN9VpAH"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "      <th>season_1</th>\n",
              "      <th>season_2</th>\n",
              "      <th>season_3</th>\n",
              "      <th>season_4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.81</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>16</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>8</td>\n",
              "      <td>32</td>\n",
              "      <td>40</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>27</td>\n",
              "      <td>32</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>10</td>\n",
              "      <td>13</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   instant     dteday  year  month  hour  holiday  weekday  workingday  \\\n",
              "0        1 2011-01-01     0      1     0        0        6           0   \n",
              "1        2 2011-01-01     0      1     1        0        6           0   \n",
              "2        3 2011-01-01     0      1     2        0        6           0   \n",
              "3        4 2011-01-01     0      1     3        0        6           0   \n",
              "4        5 2011-01-01     0      1     4        0        6           0   \n",
              "\n",
              "   weathersit  temp   atemp   hum  windspeed  casual  registered  counts  \\\n",
              "0           1  0.24  0.2879  0.81        0.0       3          13      16   \n",
              "1           1  0.22  0.2727  0.80        0.0       8          32      40   \n",
              "2           1  0.22  0.2727  0.80        0.0       5          27      32   \n",
              "3           1  0.24  0.2879  0.75        0.0       3          10      13   \n",
              "4           1  0.24  0.2879  0.75        0.0       0           1       1   \n",
              "\n",
              "   season_1  season_2  season_3  season_4  \n",
              "0         1         0         0         0  \n",
              "1         1         0         0         0  \n",
              "2         1         0         0         0  \n",
              "3         1         0         0         0  \n",
              "4         1         0         0         0  "
            ]
          },
          "execution_count": 650,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df = pd.get_dummies(hour_df, columns=['season'], dtype=int)\n",
        "hour_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 651,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "ksdZAn5gVEAY",
        "outputId": "257ed231-542e-4913-d878-584fbc84570d"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>instant</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "      <th>season_1</th>\n",
              "      <th>season_2</th>\n",
              "      <th>season_3</th>\n",
              "      <th>season_4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>0.502561</td>\n",
              "      <td>6.537775</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.028770</td>\n",
              "      <td>3.003683</td>\n",
              "      <td>0.682721</td>\n",
              "      <td>1.425283</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>35.676218</td>\n",
              "      <td>153.786869</td>\n",
              "      <td>189.463088</td>\n",
              "      <td>0.244088</td>\n",
              "      <td>0.253697</td>\n",
              "      <td>0.258703</td>\n",
              "      <td>0.243512</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5017.0295</td>\n",
              "      <td>0.500008</td>\n",
              "      <td>3.438776</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.167165</td>\n",
              "      <td>2.005771</td>\n",
              "      <td>0.465431</td>\n",
              "      <td>0.639357</td>\n",
              "      <td>0.192556</td>\n",
              "      <td>0.171850</td>\n",
              "      <td>0.192930</td>\n",
              "      <td>0.122340</td>\n",
              "      <td>49.305030</td>\n",
              "      <td>151.357286</td>\n",
              "      <td>181.387599</td>\n",
              "      <td>0.429557</td>\n",
              "      <td>0.435139</td>\n",
              "      <td>0.437935</td>\n",
              "      <td>0.429214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.020000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>4345.5000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.333300</td>\n",
              "      <td>0.480000</td>\n",
              "      <td>0.104500</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>40.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.484800</td>\n",
              "      <td>0.630000</td>\n",
              "      <td>0.194000</td>\n",
              "      <td>17.000000</td>\n",
              "      <td>115.000000</td>\n",
              "      <td>142.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>13034.5000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.660000</td>\n",
              "      <td>0.621200</td>\n",
              "      <td>0.780000</td>\n",
              "      <td>0.253700</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>220.000000</td>\n",
              "      <td>281.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.850700</td>\n",
              "      <td>367.000000</td>\n",
              "      <td>886.000000</td>\n",
              "      <td>977.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          instant          year         month          hour       holiday  \\\n",
              "count  17379.0000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean    8690.0000      0.502561      6.537775     11.546752      0.028770   \n",
              "std     5017.0295      0.500008      3.438776      6.914405      0.167165   \n",
              "min        1.0000      0.000000      1.000000      0.000000      0.000000   \n",
              "25%     4345.5000      0.000000      4.000000      6.000000      0.000000   \n",
              "50%     8690.0000      1.000000      7.000000     12.000000      0.000000   \n",
              "75%    13034.5000      1.000000     10.000000     18.000000      0.000000   \n",
              "max    17379.0000      1.000000     12.000000     23.000000      1.000000   \n",
              "\n",
              "            weekday    workingday    weathersit          temp         atemp  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       3.003683      0.682721      1.425283      0.496987      0.475775   \n",
              "std        2.005771      0.465431      0.639357      0.192556      0.171850   \n",
              "min        0.000000      0.000000      1.000000      0.020000      0.000000   \n",
              "25%        1.000000      0.000000      1.000000      0.340000      0.333300   \n",
              "50%        3.000000      1.000000      1.000000      0.500000      0.484800   \n",
              "75%        5.000000      1.000000      2.000000      0.660000      0.621200   \n",
              "max        6.000000      1.000000      4.000000      1.000000      1.000000   \n",
              "\n",
              "                hum     windspeed        casual    registered        counts  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.627229      0.190098     35.676218    153.786869    189.463088   \n",
              "std        0.192930      0.122340     49.305030    151.357286    181.387599   \n",
              "min        0.000000      0.000000      0.000000      0.000000      1.000000   \n",
              "25%        0.480000      0.104500      4.000000     34.000000     40.000000   \n",
              "50%        0.630000      0.194000     17.000000    115.000000    142.000000   \n",
              "75%        0.780000      0.253700     48.000000    220.000000    281.000000   \n",
              "max        1.000000      0.850700    367.000000    886.000000    977.000000   \n",
              "\n",
              "           season_1      season_2      season_3      season_4  \n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  \n",
              "mean       0.244088      0.253697      0.258703      0.243512  \n",
              "std        0.429557      0.435139      0.437935      0.429214  \n",
              "min        0.000000      0.000000      0.000000      0.000000  \n",
              "25%        0.000000      0.000000      0.000000      0.000000  \n",
              "50%        0.000000      0.000000      0.000000      0.000000  \n",
              "75%        0.000000      1.000000      1.000000      0.000000  \n",
              "max        1.000000      1.000000      1.000000      1.000000  "
            ]
          },
          "execution_count": 651,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gp-Y6wU38DC1"
      },
      "source": [
        "## Exploratory Data Analysis (EDA)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MW7WF2kr8DC1"
      },
      "source": [
        "### Explore Day_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 652,
      "metadata": {
        "id": "QpstFlNFiUeH"
      },
      "outputs": [],
      "source": [
        "# Menghapus kolom instan karena hanya untuk indeks\n",
        "day_df = day_df.drop(columns=['instant'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 653,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RHKm3mRgigBs",
        "outputId": "302cb69a-f3ee-46a4-939e-6b78d9c8a0af"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "dteday\n",
            "731\n",
            "2012-02-14    1\n",
            "2011-04-25    1\n",
            "2012-08-16    1\n",
            "2011-06-26    1\n",
            "2012-02-23    1\n",
            "             ..\n",
            "2012-06-02    1\n",
            "2011-04-12    1\n",
            "2012-12-15    1\n",
            "2011-06-13    1\n",
            "2011-12-14    1\n",
            "Name: dteday, Length: 731, dtype: int64\n",
            "\n",
            "year\n",
            "2\n",
            "2012    366\n",
            "2011    365\n",
            "Name: year, dtype: int64\n",
            "\n",
            "month\n",
            "12\n",
            "Oct      62\n",
            "March    62\n",
            "July     62\n",
            "Aug      62\n",
            "Dec      62\n",
            "May      62\n",
            "Jan      62\n",
            "June     60\n",
            "Nov      60\n",
            "April    60\n",
            "Sept     60\n",
            "Feb      57\n",
            "Name: month, dtype: int64\n",
            "\n",
            "weekday\n",
            "7\n",
            "Tuesday      105\n",
            "Monday       105\n",
            "Sunday       105\n",
            "Wednesday    104\n",
            "Saturday     104\n",
            "Friday       104\n",
            "Thursday     104\n",
            "Name: weekday, dtype: int64\n",
            "\n",
            "workingday\n",
            "2\n",
            "Hari Libur    500\n",
            "Hari Kerja    231\n",
            "Name: workingday, dtype: int64\n",
            "\n",
            "holiday\n",
            "2\n",
            "0    710\n",
            "1     21\n",
            "Name: holiday, dtype: int64\n",
            "\n",
            "weathersit\n",
            "3\n",
            "Clear        463\n",
            "Cloudy       247\n",
            "Snow/Rain     21\n",
            "Name: weathersit, dtype: int64\n",
            "\n",
            "season\n",
            "4\n",
            "fall      188\n",
            "summer    184\n",
            "spring    181\n",
            "winter    178\n",
            "Name: season, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "# Memeriksa kolom dteday\n",
        "print('\\ndteday')\n",
        "print(day_df.dteday.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'dteday'\n",
        "print(day_df.dteday.value_counts())  # Menampilkan distribusi nilai dalam kolom 'dteday'\n",
        "\n",
        "# Memeriksa kolom year\n",
        "print('\\nyear')\n",
        "print(day_df.year.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'year'\n",
        "print(day_df.year.value_counts())  # Menampilkan distribusi nilai dalam kolom 'year'\n",
        "\n",
        "# Memeriksa kolom month\n",
        "print('\\nmonth')\n",
        "print(day_df.month.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'month'\n",
        "print(day_df.month.value_counts())  # Menampilkan distribusi nilai dalam kolom 'month'\n",
        "\n",
        "# Memeriksa kolom weekday\n",
        "print('\\nweekday')\n",
        "print(day_df.weekday.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'weekday'\n",
        "print(day_df.weekday.value_counts())  # Menampilkan distribusi nilai dalam kolom 'weekday'\n",
        "\n",
        "# Memeriksa kolom working day\n",
        "print('\\nworkingday')\n",
        "print(day_df.workingday.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'workingday'\n",
        "print(day_df.workingday.value_counts())  # Menampilkan distribusi nilai dalam kolom 'workingday'\n",
        "\n",
        "# Memeriksa kolom holiday\n",
        "print('\\nholiday')\n",
        "print(day_df.holiday.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'holiday'\n",
        "print(day_df.holiday.value_counts())  # Menampilkan distribusi nilai dalam kolom 'holiday'\n",
        "\n",
        "# Memeriksa kolom weathersit\n",
        "print('\\nweathersit')\n",
        "print(day_df.weathersit.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'weathersit'\n",
        "print(day_df.weathersit.value_counts())  # Menampilkan distribusi nilai dalam kolom 'weathersit'\n",
        "\n",
        "# Memeriksa kolom season\n",
        "print('\\nseason')\n",
        "print(day_df.season.nunique())  # Menampilkan jumlah nilai unik dalam kolom 'season'\n",
        "print(day_df.season.value_counts())  # Menampilkan distribusi nilai dalam kolom 'season'\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 654,
      "metadata": {
        "id": "bYXMQIs1ikcD"
      },
      "outputs": [],
      "source": [
        "# Membagi variabel dalam dataset menjadi dua kelompok berdasarkan jenisnya\n",
        "\n",
        "# variabel kategorikal\n",
        "cat_vars = ['season', 'year', 'month', 'weekday', 'workingday', 'weathersit']\n",
        "\n",
        "# variabel numerik\n",
        "num_vars = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'counts']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 655,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "UEx8XPGQi0Fi",
        "outputId": "fd408dd9-0dc9-48c1-9188-dd4d2238ede0"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Sunday</td>\n",
              "      <td>Hari Kerja</td>\n",
              "      <td>Cloudy</td>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>0.160446</td>\n",
              "      <td>331</td>\n",
              "      <td>654</td>\n",
              "      <td>985</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2011-01-02</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Monday</td>\n",
              "      <td>Hari Kerja</td>\n",
              "      <td>Cloudy</td>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>0.248539</td>\n",
              "      <td>131</td>\n",
              "      <td>670</td>\n",
              "      <td>801</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2011-01-03</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Tuesday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>0.248309</td>\n",
              "      <td>120</td>\n",
              "      <td>1229</td>\n",
              "      <td>1349</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2011-01-04</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Wednesday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>0.160296</td>\n",
              "      <td>108</td>\n",
              "      <td>1454</td>\n",
              "      <td>1562</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2011-01-05</td>\n",
              "      <td>spring</td>\n",
              "      <td>2011</td>\n",
              "      <td>Jan</td>\n",
              "      <td>0</td>\n",
              "      <td>Thursday</td>\n",
              "      <td>Hari Libur</td>\n",
              "      <td>Clear</td>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>0.186900</td>\n",
              "      <td>82</td>\n",
              "      <td>1518</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      dteday  season  year month  holiday    weekday  workingday weathersit  \\\n",
              "0 2011-01-01  spring  2011   Jan        0     Sunday  Hari Kerja     Cloudy   \n",
              "1 2011-01-02  spring  2011   Jan        0     Monday  Hari Kerja     Cloudy   \n",
              "2 2011-01-03  spring  2011   Jan        0    Tuesday  Hari Libur      Clear   \n",
              "3 2011-01-04  spring  2011   Jan        0  Wednesday  Hari Libur      Clear   \n",
              "4 2011-01-05  spring  2011   Jan        0   Thursday  Hari Libur      Clear   \n",
              "\n",
              "       temp     atemp       hum  windspeed  casual  registered  counts  \n",
              "0  0.344167  0.363625  0.805833   0.160446     331         654     985  \n",
              "1  0.363478  0.353739  0.696087   0.248539     131         670     801  \n",
              "2  0.196364  0.189405  0.437273   0.248309     120        1229    1349  \n",
              "3  0.200000  0.212122  0.590435   0.160296     108        1454    1562  \n",
              "4  0.226957  0.229270  0.436957   0.186900      82        1518    1600  "
            ]
          },
          "execution_count": 655,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 656,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YJnN_fowj4-b",
        "outputId": "b11ef3f9-a915-4bcb-bc1b-989486c1d8a5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count    731.000000\n",
              "mean       0.190486\n",
              "std        0.077498\n",
              "min        0.022392\n",
              "25%        0.134950\n",
              "50%        0.180975\n",
              "75%        0.233214\n",
              "max        0.507463\n",
              "Name: windspeed, dtype: float64"
            ]
          },
          "execution_count": 656,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.windspeed.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 657,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZFXeP-tZj46U",
        "outputId": "45181812-7512-4513-947b-1c04d60f598c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count    731.000000\n",
              "mean       0.495385\n",
              "std        0.183051\n",
              "min        0.059130\n",
              "25%        0.337083\n",
              "50%        0.498333\n",
              "75%        0.655417\n",
              "max        0.861667\n",
              "Name: temp, dtype: float64"
            ]
          },
          "execution_count": 657,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.temp.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 658,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O2Up0LUKj410",
        "outputId": "bce4d9b2-d6a6-4b7c-ded7-529d039068a7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count    731.000000\n",
              "mean       0.474354\n",
              "std        0.162961\n",
              "min        0.079070\n",
              "25%        0.337842\n",
              "50%        0.486733\n",
              "75%        0.608602\n",
              "max        0.840896\n",
              "Name: atemp, dtype: float64"
            ]
          },
          "execution_count": 658,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.atemp.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 659,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CT2m1l0cj4yD",
        "outputId": "932d025c-a21d-41d1-d4b2-5e7c9a0e904c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count    731.000000\n",
              "mean       0.627894\n",
              "std        0.142429\n",
              "min        0.000000\n",
              "25%        0.520000\n",
              "50%        0.626667\n",
              "75%        0.730209\n",
              "max        0.972500\n",
              "Name: hum, dtype: float64"
            ]
          },
          "execution_count": 659,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.hum.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 660,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ckVF50DMkHZF",
        "outputId": "03dd0e25-d43c-4ea7-ffd5-fd6e95e3c9ab"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count     731.000000\n",
              "mean     4504.348837\n",
              "std      1937.211452\n",
              "min        22.000000\n",
              "25%      3152.000000\n",
              "50%      4548.000000\n",
              "75%      5956.000000\n",
              "max      8714.000000\n",
              "Name: counts, dtype: float64"
            ]
          },
          "execution_count": 660,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.counts.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 661,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qGaZuACtkHV8",
        "outputId": "c69c7977-6cfe-4502-d0b7-9a7c4bbccd45"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count     731.000000\n",
              "mean      848.176471\n",
              "std       686.622488\n",
              "min         2.000000\n",
              "25%       315.500000\n",
              "50%       713.000000\n",
              "75%      1096.000000\n",
              "max      3410.000000\n",
              "Name: casual, dtype: float64"
            ]
          },
          "execution_count": 661,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.casual.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 662,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GvDKfqGnkHSD",
        "outputId": "c52d46cc-7e2f-4112-c715-ff9d98bf9edc"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "count     731.000000\n",
              "mean     3656.172367\n",
              "std      1560.256377\n",
              "min        20.000000\n",
              "25%      2497.000000\n",
              "50%      3662.000000\n",
              "75%      4776.500000\n",
              "max      6946.000000\n",
              "Name: registered, dtype: float64"
            ]
          },
          "execution_count": 662,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "day_df.registered.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fODe-OuwaDkr"
      },
      "source": [
        "### Explore Hour_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 663,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Menghapus kolom instan karena hanya untuk indeks\n",
        "hour_df = hour_df.drop(columns=['instant'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 664,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "e9CQCZjk8DC2",
        "outputId": "c59882c3-a162-4f89-b5d9-6a2519bcc3d5"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "      <th>season_1</th>\n",
              "      <th>season_2</th>\n",
              "      <th>season_3</th>\n",
              "      <th>season_4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>0.502561</td>\n",
              "      <td>6.537775</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.028770</td>\n",
              "      <td>3.003683</td>\n",
              "      <td>0.682721</td>\n",
              "      <td>1.425283</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>35.676218</td>\n",
              "      <td>153.786869</td>\n",
              "      <td>189.463088</td>\n",
              "      <td>0.244088</td>\n",
              "      <td>0.253697</td>\n",
              "      <td>0.258703</td>\n",
              "      <td>0.243512</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.500008</td>\n",
              "      <td>3.438776</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.167165</td>\n",
              "      <td>2.005771</td>\n",
              "      <td>0.465431</td>\n",
              "      <td>0.639357</td>\n",
              "      <td>0.192556</td>\n",
              "      <td>0.171850</td>\n",
              "      <td>0.192930</td>\n",
              "      <td>0.122340</td>\n",
              "      <td>49.305030</td>\n",
              "      <td>151.357286</td>\n",
              "      <td>181.387599</td>\n",
              "      <td>0.429557</td>\n",
              "      <td>0.435139</td>\n",
              "      <td>0.437935</td>\n",
              "      <td>0.429214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.020000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.333300</td>\n",
              "      <td>0.480000</td>\n",
              "      <td>0.104500</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>40.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.484800</td>\n",
              "      <td>0.630000</td>\n",
              "      <td>0.194000</td>\n",
              "      <td>17.000000</td>\n",
              "      <td>115.000000</td>\n",
              "      <td>142.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.660000</td>\n",
              "      <td>0.621200</td>\n",
              "      <td>0.780000</td>\n",
              "      <td>0.253700</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>220.000000</td>\n",
              "      <td>281.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.850700</td>\n",
              "      <td>367.000000</td>\n",
              "      <td>886.000000</td>\n",
              "      <td>977.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "               year         month          hour       holiday       weekday  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.502561      6.537775     11.546752      0.028770      3.003683   \n",
              "std        0.500008      3.438776      6.914405      0.167165      2.005771   \n",
              "min        0.000000      1.000000      0.000000      0.000000      0.000000   \n",
              "25%        0.000000      4.000000      6.000000      0.000000      1.000000   \n",
              "50%        1.000000      7.000000     12.000000      0.000000      3.000000   \n",
              "75%        1.000000     10.000000     18.000000      0.000000      5.000000   \n",
              "max        1.000000     12.000000     23.000000      1.000000      6.000000   \n",
              "\n",
              "         workingday    weathersit          temp         atemp           hum  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.682721      1.425283      0.496987      0.475775      0.627229   \n",
              "std        0.465431      0.639357      0.192556      0.171850      0.192930   \n",
              "min        0.000000      1.000000      0.020000      0.000000      0.000000   \n",
              "25%        0.000000      1.000000      0.340000      0.333300      0.480000   \n",
              "50%        1.000000      1.000000      0.500000      0.484800      0.630000   \n",
              "75%        1.000000      2.000000      0.660000      0.621200      0.780000   \n",
              "max        1.000000      4.000000      1.000000      1.000000      1.000000   \n",
              "\n",
              "          windspeed        casual    registered        counts      season_1  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.190098     35.676218    153.786869    189.463088      0.244088   \n",
              "std        0.122340     49.305030    151.357286    181.387599      0.429557   \n",
              "min        0.000000      0.000000      0.000000      1.000000      0.000000   \n",
              "25%        0.104500      4.000000     34.000000     40.000000      0.000000   \n",
              "50%        0.194000     17.000000    115.000000    142.000000      0.000000   \n",
              "75%        0.253700     48.000000    220.000000    281.000000      0.000000   \n",
              "max        0.850700    367.000000    886.000000    977.000000      1.000000   \n",
              "\n",
              "           season_2      season_3      season_4  \n",
              "count  17379.000000  17379.000000  17379.000000  \n",
              "mean       0.253697      0.258703      0.243512  \n",
              "std        0.435139      0.437935      0.429214  \n",
              "min        0.000000      0.000000      0.000000  \n",
              "25%        0.000000      0.000000      0.000000  \n",
              "50%        0.000000      0.000000      0.000000  \n",
              "75%        1.000000      1.000000      0.000000  \n",
              "max        1.000000      1.000000      1.000000  "
            ]
          },
          "execution_count": 664,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 665,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oIvMbzbmjloU",
        "outputId": "a8604273-82c8-4c51-b898-16db82710876"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17379 entries, 0 to 17378\n",
            "Data columns (total 19 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   dteday      17379 non-null  datetime64[ns]\n",
            " 1   year        17379 non-null  int64         \n",
            " 2   month       17379 non-null  int64         \n",
            " 3   hour        17379 non-null  int64         \n",
            " 4   holiday     17379 non-null  int64         \n",
            " 5   weekday     17379 non-null  int64         \n",
            " 6   workingday  17379 non-null  int64         \n",
            " 7   weathersit  17379 non-null  int64         \n",
            " 8   temp        17379 non-null  float64       \n",
            " 9   atemp       17379 non-null  float64       \n",
            " 10  hum         17379 non-null  float64       \n",
            " 11  windspeed   17379 non-null  float64       \n",
            " 12  casual      17379 non-null  int64         \n",
            " 13  registered  17379 non-null  int64         \n",
            " 14  counts      17379 non-null  int64         \n",
            " 15  season_1    17379 non-null  int32         \n",
            " 16  season_2    17379 non-null  int32         \n",
            " 17  season_3    17379 non-null  int32         \n",
            " 18  season_4    17379 non-null  int32         \n",
            "dtypes: datetime64[ns](1), float64(4), int32(4), int64(10)\n",
            "memory usage: 2.3 MB\n",
            "None\n"
          ]
        }
      ],
      "source": [
        "print(hour_df.info())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 666,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oPn3FH6tSo7U",
        "outputId": "5e089199-b82a-4551-c8fa-db65681668a9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Perbandingan kategori pada hari kerja (workingday):\n",
            "workingday\n",
            "0    181.405332\n",
            "1    193.207754\n",
            "Name: counts, dtype: float64\n"
          ]
        }
      ],
      "source": [
        "# Perbandingan kategori pada hari kerja (workingday)\n",
        "print(\"Perbandingan kategori pada hari kerja (workingday):\")\n",
        "print(hour_df.groupby('workingday')['counts'].mean())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 667,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "06vszTP_UEik",
        "outputId": "aeaf66f6-2bee-497f-d170-718ec7f9600a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Distribusi variabel numerik:\n",
            "               temp         atemp           hum     windspeed        casual  \\\n",
            "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
            "mean       0.496987      0.475775      0.627229      0.190098     35.676218   \n",
            "std        0.192556      0.171850      0.192930      0.122340     49.305030   \n",
            "min        0.020000      0.000000      0.000000      0.000000      0.000000   \n",
            "25%        0.340000      0.333300      0.480000      0.104500      4.000000   \n",
            "50%        0.500000      0.484800      0.630000      0.194000     17.000000   \n",
            "75%        0.660000      0.621200      0.780000      0.253700     48.000000   \n",
            "max        1.000000      1.000000      1.000000      0.850700    367.000000   \n",
            "\n",
            "         registered        counts  \n",
            "count  17379.000000  17379.000000  \n",
            "mean     153.786869    189.463088  \n",
            "std      151.357286    181.387599  \n",
            "min        0.000000      1.000000  \n",
            "25%       34.000000     40.000000  \n",
            "50%      115.000000    142.000000  \n",
            "75%      220.000000    281.000000  \n",
            "max      886.000000    977.000000  \n",
            "Distribusi variabel kategorikal:\n",
            "season_1  season_2  season_3  season_4\n",
            "0         0         1         0           4496\n",
            "          1         0         0           4409\n",
            "1         0         0         0           4242\n",
            "0         0         0         1           4232\n",
            "dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(\"Distribusi variabel numerik:\")\n",
        "print(hour_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'counts']].describe())\n",
        "\n",
        "print(\"Distribusi variabel kategorikal:\")\n",
        "print(hour_df[['season_1','season_2','season_3','season_4']].value_counts())\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 668,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3uKB6F8yUfxH",
        "outputId": "6754e8b9-02da-4678-d3d4-f1a88c4366ba"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Korelasi matriks:\n",
            "                year     month      hour   holiday   weekday  workingday  \\\n",
            "year        1.000000 -0.010473 -0.003867  0.006692 -0.004485   -0.002196   \n",
            "month      -0.010473  1.000000 -0.005772  0.018430  0.010400   -0.003477   \n",
            "hour       -0.003867 -0.005772  1.000000  0.000479 -0.003498    0.002285   \n",
            "holiday     0.006692  0.018430  0.000479  1.000000 -0.102088   -0.252471   \n",
            "weekday    -0.004485  0.010400 -0.003498 -0.102088  1.000000    0.035955   \n",
            "workingday -0.002196 -0.003477  0.002285 -0.252471  0.035955    1.000000   \n",
            "weathersit -0.019157  0.005400 -0.020203 -0.017036  0.003311    0.044672   \n",
            "temp        0.040913  0.201691  0.137603 -0.027340 -0.001795    0.055390   \n",
            "atemp       0.039222  0.208096  0.133750 -0.030973 -0.008821    0.054667   \n",
            "hum        -0.083546  0.164411 -0.276498 -0.010588 -0.037158    0.015688   \n",
            "windspeed  -0.008740 -0.135386  0.137252  0.003988  0.011502   -0.011830   \n",
            "casual      0.142779  0.068457  0.301202  0.031564  0.032721   -0.300942   \n",
            "registered  0.253684  0.122273  0.374141 -0.047345  0.021578    0.134326   \n",
            "counts      0.250495  0.120638  0.394071 -0.030927  0.026900    0.030284   \n",
            "season_1    0.011290 -0.564834  0.008363  0.033622  0.001428   -0.029387   \n",
            "season_2   -0.002589 -0.319382 -0.002919 -0.024404 -0.003510    0.015879   \n",
            "season_3   -0.000923  0.197900 -0.003348 -0.026216  0.008676    0.020182   \n",
            "season_4   -0.007732  0.687155 -0.001994  0.017840 -0.006723   -0.007280   \n",
            "\n",
            "            weathersit      temp     atemp       hum  windspeed    casual  \\\n",
            "year         -0.019157  0.040913  0.039222 -0.083546  -0.008740  0.142779   \n",
            "month         0.005400  0.201691  0.208096  0.164411  -0.135386  0.068457   \n",
            "hour         -0.020203  0.137603  0.133750 -0.276498   0.137252  0.301202   \n",
            "holiday      -0.017036 -0.027340 -0.030973 -0.010588   0.003988  0.031564   \n",
            "weekday       0.003311 -0.001795 -0.008821 -0.037158   0.011502  0.032721   \n",
            "workingday    0.044672  0.055390  0.054667  0.015688  -0.011830 -0.300942   \n",
            "weathersit    1.000000 -0.102640 -0.105563  0.418130   0.026226 -0.152628   \n",
            "temp         -0.102640  1.000000  0.987672 -0.069881  -0.023125  0.459616   \n",
            "atemp        -0.105563  0.987672  1.000000 -0.051918  -0.062336  0.454080   \n",
            "hum           0.418130 -0.069881 -0.051918  1.000000  -0.290105 -0.347028   \n",
            "windspeed     0.026226 -0.023125 -0.062336 -0.290105   1.000000  0.090287   \n",
            "casual       -0.152628  0.459616  0.454080 -0.347028   0.090287  1.000000   \n",
            "registered   -0.120966  0.335361  0.332559 -0.273933   0.082321  0.506618   \n",
            "counts       -0.142426  0.404772  0.400929 -0.322911   0.093234  0.694564   \n",
            "season_1      0.030999 -0.583859 -0.587470 -0.135138   0.116168 -0.246476   \n",
            "season_2      0.016738  0.144363  0.151903 -0.000625   0.063447  0.123983   \n",
            "season_3     -0.087771  0.642516  0.619570  0.018184  -0.089358  0.175067   \n",
            "season_4      0.041561 -0.217601 -0.198218  0.117326  -0.089410 -0.057646   \n",
            "\n",
            "            registered    counts  season_1  season_2  season_3  season_4  \n",
            "year          0.253684  0.250495  0.011290 -0.002589 -0.000923 -0.007732  \n",
            "month         0.122273  0.120638 -0.564834 -0.319382  0.197900  0.687155  \n",
            "hour          0.374141  0.394071  0.008363 -0.002919 -0.003348 -0.001994  \n",
            "holiday      -0.047345 -0.030927  0.033622 -0.024404 -0.026216  0.017840  \n",
            "weekday       0.021578  0.026900  0.001428 -0.003510  0.008676 -0.006723  \n",
            "workingday    0.134326  0.030284 -0.029387  0.015879  0.020182 -0.007280  \n",
            "weathersit   -0.120966 -0.142426  0.030999  0.016738 -0.087771  0.041561  \n",
            "temp          0.335361  0.404772 -0.583859  0.144363  0.642516 -0.217601  \n",
            "atemp         0.332559  0.400929 -0.587470  0.151903  0.619570 -0.198218  \n",
            "hum          -0.273933 -0.322911 -0.135138 -0.000625  0.018184  0.117326  \n",
            "windspeed     0.082321  0.093234  0.116168  0.063447 -0.089358 -0.089410  \n",
            "casual        0.506618  0.694564 -0.246476  0.123983  0.175067 -0.057646  \n",
            "registered    1.000000  0.972151 -0.213866  0.032345  0.124675  0.054037  \n",
            "counts        0.972151  1.000000 -0.245456  0.060692  0.151621  0.029421  \n",
            "season_1     -0.213866 -0.245456  1.000000 -0.331312 -0.335693 -0.322401  \n",
            "season_2      0.032345  0.060692 -0.331312  1.000000 -0.344433 -0.330795  \n",
            "season_3      0.124675  0.151621 -0.335693 -0.344433  1.000000 -0.335169  \n",
            "season_4      0.054037  0.029421 -0.322401 -0.330795 -0.335169  1.000000  \n"
          ]
        }
      ],
      "source": [
        "# Korelasi Antara Variabel\n",
        "correlation_matrix = hour_df.corr()\n",
        "print(\"Korelasi matriks:\")\n",
        "print(correlation_matrix)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 669,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "3292679"
            ]
          },
          "execution_count": 669,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hour_df['counts'].sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Explore All-df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 709,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "# Pastikan tidak ada data yang duplicate sebelum di merge\n",
        "print(day_df.duplicated('dteday').sum())\n",
        "print(hour_df.duplicated('dteday').sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 711,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Jika ada maka hapus duplikasi hingga 0\n",
        "day_df = day_df.drop_duplicates('dteday')\n",
        "hour_df = hour_df.drop_duplicates('dteday')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 707,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Merge DataFrame dengan memastikan kolom 'dteday' dan 'hour' unik\n",
        "all_df = pd.merge(day_df, hour_df[['dteday', 'hour', 'season_1', 'season_2', 'season_3', 'season_4']], how='inner', on='dteday')\n",
        "\n",
        "# Berikan sufiks yang berbeda untuk kolom yang memiliki nama yang sama\n",
        "all_df['hour'] = hour_df['hour']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 698,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>holiday</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "      <th>hour</th>\n",
              "      <th>season_1</th>\n",
              "      <th>season_2</th>\n",
              "      <th>season_3</th>\n",
              "      <th>season_4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>0.028770</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>854.339720</td>\n",
              "      <td>3679.353242</td>\n",
              "      <td>4533.692963</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.244088</td>\n",
              "      <td>0.253697</td>\n",
              "      <td>0.258703</td>\n",
              "      <td>0.243512</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.167165</td>\n",
              "      <td>0.182445</td>\n",
              "      <td>0.162426</td>\n",
              "      <td>0.141779</td>\n",
              "      <td>0.077204</td>\n",
              "      <td>685.686754</td>\n",
              "      <td>1544.953518</td>\n",
              "      <td>1917.376947</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.429557</td>\n",
              "      <td>0.435139</td>\n",
              "      <td>0.437935</td>\n",
              "      <td>0.429214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.059130</td>\n",
              "      <td>0.079070</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.022392</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>22.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.338363</td>\n",
              "      <td>0.520000</td>\n",
              "      <td>0.134950</td>\n",
              "      <td>318.000000</td>\n",
              "      <td>2545.000000</td>\n",
              "      <td>3214.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.502500</td>\n",
              "      <td>0.490122</td>\n",
              "      <td>0.625833</td>\n",
              "      <td>0.180967</td>\n",
              "      <td>724.000000</td>\n",
              "      <td>3681.000000</td>\n",
              "      <td>4563.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.655833</td>\n",
              "      <td>0.610488</td>\n",
              "      <td>0.729583</td>\n",
              "      <td>0.233204</td>\n",
              "      <td>1100.000000</td>\n",
              "      <td>4801.000000</td>\n",
              "      <td>5986.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.861667</td>\n",
              "      <td>0.840896</td>\n",
              "      <td>0.972500</td>\n",
              "      <td>0.507463</td>\n",
              "      <td>3410.000000</td>\n",
              "      <td>6946.000000</td>\n",
              "      <td>8714.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            holiday          temp         atemp           hum     windspeed  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.028770      0.496987      0.475775      0.627229      0.190098   \n",
              "std        0.167165      0.182445      0.162426      0.141779      0.077204   \n",
              "min        0.000000      0.059130      0.079070      0.000000      0.022392   \n",
              "25%        0.000000      0.340000      0.338363      0.520000      0.134950   \n",
              "50%        0.000000      0.502500      0.490122      0.625833      0.180967   \n",
              "75%        0.000000      0.655833      0.610488      0.729583      0.233204   \n",
              "max        1.000000      0.861667      0.840896      0.972500      0.507463   \n",
              "\n",
              "             casual    registered        counts          hour      season_1  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean     854.339720   3679.353242   4533.692963     11.546752      0.244088   \n",
              "std      685.686754   1544.953518   1917.376947      6.914405      0.429557   \n",
              "min        2.000000     20.000000     22.000000      0.000000      0.000000   \n",
              "25%      318.000000   2545.000000   3214.000000      6.000000      0.000000   \n",
              "50%      724.000000   3681.000000   4563.000000     12.000000      0.000000   \n",
              "75%     1100.000000   4801.000000   5986.000000     18.000000      0.000000   \n",
              "max     3410.000000   6946.000000   8714.000000     23.000000      1.000000   \n",
              "\n",
              "           season_2      season_3      season_4  \n",
              "count  17379.000000  17379.000000  17379.000000  \n",
              "mean       0.253697      0.258703      0.243512  \n",
              "std        0.435139      0.437935      0.429214  \n",
              "min        0.000000      0.000000      0.000000  \n",
              "25%        0.000000      0.000000      0.000000  \n",
              "50%        0.000000      0.000000      0.000000  \n",
              "75%        1.000000      1.000000      0.000000  \n",
              "max        1.000000      1.000000      1.000000  "
            ]
          },
          "execution_count": 698,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 699,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 17379 entries, 0 to 17378\n",
            "Data columns (total 20 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   dteday      17379 non-null  datetime64[ns]\n",
            " 1   season      17379 non-null  object        \n",
            " 2   year        17379 non-null  object        \n",
            " 3   month       17379 non-null  object        \n",
            " 4   holiday     17379 non-null  int64         \n",
            " 5   weekday     17379 non-null  object        \n",
            " 6   workingday  17379 non-null  object        \n",
            " 7   weathersit  17379 non-null  object        \n",
            " 8   temp        17379 non-null  float64       \n",
            " 9   atemp       17379 non-null  float64       \n",
            " 10  hum         17379 non-null  float64       \n",
            " 11  windspeed   17379 non-null  float64       \n",
            " 12  casual      17379 non-null  int64         \n",
            " 13  registered  17379 non-null  int64         \n",
            " 14  counts      17379 non-null  int64         \n",
            " 15  hour        17379 non-null  int64         \n",
            " 16  season_1    17379 non-null  int32         \n",
            " 17  season_2    17379 non-null  int32         \n",
            " 18  season_3    17379 non-null  int32         \n",
            " 19  season_4    17379 non-null  int32         \n",
            "dtypes: datetime64[ns](1), float64(4), int32(4), int64(5), object(6)\n",
            "memory usage: 2.5+ MB\n"
          ]
        }
      ],
      "source": [
        "all_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 708,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "3292679"
            ]
          },
          "execution_count": 708,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df['counts'].sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 674,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Unique values in 'counts': 696\n"
          ]
        }
      ],
      "source": [
        "print(\"Unique values in 'counts':\", len(all_df['counts'].unique()))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 675,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 17379 entries, 0 to 17378\n",
            "Data columns (total 20 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   dteday      17379 non-null  datetime64[ns]\n",
            " 1   season      17379 non-null  object        \n",
            " 2   year        17379 non-null  object        \n",
            " 3   month       17379 non-null  object        \n",
            " 4   holiday     17379 non-null  int64         \n",
            " 5   weekday     17379 non-null  object        \n",
            " 6   workingday  17379 non-null  object        \n",
            " 7   weathersit  17379 non-null  object        \n",
            " 8   temp        17379 non-null  float64       \n",
            " 9   atemp       17379 non-null  float64       \n",
            " 10  hum         17379 non-null  float64       \n",
            " 11  windspeed   17379 non-null  float64       \n",
            " 12  casual      17379 non-null  int64         \n",
            " 13  registered  17379 non-null  int64         \n",
            " 14  counts      17379 non-null  int64         \n",
            " 15  hour        17379 non-null  int64         \n",
            " 16  season_1    17379 non-null  int32         \n",
            " 17  season_2    17379 non-null  int32         \n",
            " 18  season_3    17379 non-null  int32         \n",
            " 19  season_4    17379 non-null  int32         \n",
            "dtypes: datetime64[ns](1), float64(4), int32(4), int64(5), object(6)\n",
            "memory usage: 2.5+ MB\n"
          ]
        }
      ],
      "source": [
        "all_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 676,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>counts</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2011-01-01</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>23640</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2011-01-02</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>18423</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2011-01-03</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>29678</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2011-01-04</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>35926</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2011-01-05</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>36800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012-12-27</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.254167</td>\n",
              "      <td>0.226642</td>\n",
              "      <td>0.652917</td>\n",
              "      <td>50736</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012-12-28</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.253333</td>\n",
              "      <td>0.255046</td>\n",
              "      <td>0.590000</td>\n",
              "      <td>74280</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012-12-29</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.253333</td>\n",
              "      <td>0.242400</td>\n",
              "      <td>0.752917</td>\n",
              "      <td>32184</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012-12-30</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.255833</td>\n",
              "      <td>0.231700</td>\n",
              "      <td>0.483333</td>\n",
              "      <td>43104</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012-12-31</th>\n",
              "      <th>spring</th>\n",
              "      <td>0.215833</td>\n",
              "      <td>0.223487</td>\n",
              "      <td>0.577500</td>\n",
              "      <td>65496</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>731 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                       temp     atemp       hum  counts\n",
              "dteday     season                                      \n",
              "2011-01-01 spring  0.344167  0.363625  0.805833   23640\n",
              "2011-01-02 spring  0.363478  0.353739  0.696087   18423\n",
              "2011-01-03 spring  0.196364  0.189405  0.437273   29678\n",
              "2011-01-04 spring  0.200000  0.212122  0.590435   35926\n",
              "2011-01-05 spring  0.226957  0.229270  0.436957   36800\n",
              "...                     ...       ...       ...     ...\n",
              "2012-12-27 spring  0.254167  0.226642  0.652917   50736\n",
              "2012-12-28 spring  0.253333  0.255046  0.590000   74280\n",
              "2012-12-29 spring  0.253333  0.242400  0.752917   32184\n",
              "2012-12-30 spring  0.255833  0.231700  0.483333   43104\n",
              "2012-12-31 spring  0.215833  0.223487  0.577500   65496\n",
              "\n",
              "[731 rows x 4 columns]"
            ]
          },
          "execution_count": 676,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.groupby(by=[\"dteday\", \"season\"]).agg({\n",
        "    \"temp\": \"mean\",\n",
        "    \"atemp\": \"mean\",\n",
        "    \"hum\": \"mean\",\n",
        "    \"counts\": \"sum\"\n",
        "})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 677,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>holiday</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>counts</th>\n",
              "      <th>hour</th>\n",
              "      <th>season_1</th>\n",
              "      <th>season_2</th>\n",
              "      <th>season_3</th>\n",
              "      <th>season_4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>0.028770</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>854.339720</td>\n",
              "      <td>3679.353242</td>\n",
              "      <td>4533.692963</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.244088</td>\n",
              "      <td>0.253697</td>\n",
              "      <td>0.258703</td>\n",
              "      <td>0.243512</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.167165</td>\n",
              "      <td>0.182445</td>\n",
              "      <td>0.162426</td>\n",
              "      <td>0.141779</td>\n",
              "      <td>0.077204</td>\n",
              "      <td>685.686754</td>\n",
              "      <td>1544.953518</td>\n",
              "      <td>1917.376947</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.429557</td>\n",
              "      <td>0.435139</td>\n",
              "      <td>0.437935</td>\n",
              "      <td>0.429214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.059130</td>\n",
              "      <td>0.079070</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.022392</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>22.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.338363</td>\n",
              "      <td>0.520000</td>\n",
              "      <td>0.134950</td>\n",
              "      <td>318.000000</td>\n",
              "      <td>2545.000000</td>\n",
              "      <td>3214.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.502500</td>\n",
              "      <td>0.490122</td>\n",
              "      <td>0.625833</td>\n",
              "      <td>0.180967</td>\n",
              "      <td>724.000000</td>\n",
              "      <td>3681.000000</td>\n",
              "      <td>4563.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.655833</td>\n",
              "      <td>0.610488</td>\n",
              "      <td>0.729583</td>\n",
              "      <td>0.233204</td>\n",
              "      <td>1100.000000</td>\n",
              "      <td>4801.000000</td>\n",
              "      <td>5986.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.861667</td>\n",
              "      <td>0.840896</td>\n",
              "      <td>0.972500</td>\n",
              "      <td>0.507463</td>\n",
              "      <td>3410.000000</td>\n",
              "      <td>6946.000000</td>\n",
              "      <td>8714.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            holiday          temp         atemp           hum     windspeed  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.028770      0.496987      0.475775      0.627229      0.190098   \n",
              "std        0.167165      0.182445      0.162426      0.141779      0.077204   \n",
              "min        0.000000      0.059130      0.079070      0.000000      0.022392   \n",
              "25%        0.000000      0.340000      0.338363      0.520000      0.134950   \n",
              "50%        0.000000      0.502500      0.490122      0.625833      0.180967   \n",
              "75%        0.000000      0.655833      0.610488      0.729583      0.233204   \n",
              "max        1.000000      0.861667      0.840896      0.972500      0.507463   \n",
              "\n",
              "             casual    registered        counts          hour      season_1  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean     854.339720   3679.353242   4533.692963     11.546752      0.244088   \n",
              "std      685.686754   1544.953518   1917.376947      6.914405      0.429557   \n",
              "min        2.000000     20.000000     22.000000      0.000000      0.000000   \n",
              "25%      318.000000   2545.000000   3214.000000      6.000000      0.000000   \n",
              "50%      724.000000   3681.000000   4563.000000     12.000000      0.000000   \n",
              "75%     1100.000000   4801.000000   5986.000000     18.000000      0.000000   \n",
              "max     3410.000000   6946.000000   8714.000000     23.000000      1.000000   \n",
              "\n",
              "           season_2      season_3      season_4  \n",
              "count  17379.000000  17379.000000  17379.000000  \n",
              "mean       0.253697      0.258703      0.243512  \n",
              "std        0.435139      0.437935      0.429214  \n",
              "min        0.000000      0.000000      0.000000  \n",
              "25%        0.000000      0.000000      0.000000  \n",
              "50%        0.000000      0.000000      0.000000  \n",
              "75%        1.000000      1.000000      0.000000  \n",
              "max        1.000000      1.000000      1.000000  "
            ]
          },
          "execution_count": 677,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 678,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "4098    48\n",
              "4401    48\n",
              "2425    48\n",
              "5409    48\n",
              "6591    48\n",
              "        ..\n",
              "4334    17\n",
              "506     16\n",
              "683     12\n",
              "431      8\n",
              "22       1\n",
              "Name: counts, Length: 696, dtype: int64"
            ]
          },
          "execution_count": 678,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.counts.value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 679,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "fall      4496\n",
              "summer    4409\n",
              "spring    4242\n",
              "winter    4232\n",
              "Name: season, dtype: int64"
            ]
          },
          "execution_count": 679,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.season.value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 680,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "78791050"
            ]
          },
          "execution_count": 680,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all_df.counts.sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 682,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 17379 entries, 0 to 17378\n",
            "Data columns (total 20 columns):\n",
            " #   Column      Non-Null Count  Dtype         \n",
            "---  ------      --------------  -----         \n",
            " 0   dteday      17379 non-null  datetime64[ns]\n",
            " 1   season      17379 non-null  object        \n",
            " 2   year        17379 non-null  object        \n",
            " 3   month       17379 non-null  object        \n",
            " 4   holiday     17379 non-null  int64         \n",
            " 5   weekday     17379 non-null  object        \n",
            " 6   workingday  17379 non-null  object        \n",
            " 7   weathersit  17379 non-null  object        \n",
            " 8   temp        17379 non-null  float64       \n",
            " 9   atemp       17379 non-null  float64       \n",
            " 10  hum         17379 non-null  float64       \n",
            " 11  windspeed   17379 non-null  float64       \n",
            " 12  casual      17379 non-null  int64         \n",
            " 13  registered  17379 non-null  int64         \n",
            " 14  counts      17379 non-null  int64         \n",
            " 15  hour        17379 non-null  int64         \n",
            " 16  season_1    17379 non-null  int32         \n",
            " 17  season_2    17379 non-null  int32         \n",
            " 18  season_3    17379 non-null  int32         \n",
            " 19  season_4    17379 non-null  int32         \n",
            "dtypes: datetime64[ns](1), float64(4), int32(4), int64(5), object(6)\n",
            "memory usage: 2.5+ MB\n"
          ]
        }
      ],
      "source": [
        "all_df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 683,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Jumlah duplikasi:  0\n"
          ]
        }
      ],
      "source": [
        "print(\"Jumlah duplikasi: \", all_df.duplicated().sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 681,
      "metadata": {},
      "outputs": [],
      "source": [
        "all_df.to_csv('all_data.csv', index=False)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zsyZjqak8DC2"
      },
      "source": [
        "## Visualization & Explanatory Analysis"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 747,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "bs0aIHqjaRmE",
        "outputId": "6ab6d9ce-cdad-4b6e-b2b2-7ab56691bac6"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 576x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Pola Penggunaan Penyewaan Sepeda pada Hari Kerja vs Hari Libur\n",
        "all_type_counts = all_df['workingday'].value_counts()\n",
        "\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x=all_type_counts.index, y=all_type_counts.values, palette='viridis')\n",
        "\n",
        "plt.xlabel('Hari')\n",
        "plt.ylabel('Jumlah Penyewaan')\n",
        "plt.title('Pola Penggunaan Penyewaan Sepeda pada Hari Kerja vs Hari Libur')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 713,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 632
        },
        "id": "Bdql4x2fVEa_",
        "outputId": "8b0610ee-7842-46d1-c6a6-243f473fb06e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "Analisis tren dari waktu ke waktu:\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<AxesSubplot:title={'center':'Tren Penyewaan Sepeda dari Waktu ke Waktu'}, xlabel='dteday'>"
            ]
          },
          "execution_count": 713,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Analisis Tren Waktu\n",
        "print(\"\\nAnalisis tren dari waktu ke waktu:\")\n",
        "all_df.set_index('dteday')['counts'].plot(figsize=(12, 6), title='Tren Penyewaan Sepeda dari Waktu ke Waktu')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 714,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 630
        },
        "id": "EhQNFrR3jqq_",
        "outputId": "94d84bf4-ac14-4d01-d2bd-80ed4fbbf361"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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LBgYJblZkgP76Q6aGH5lksdOqygAAAAAxrNgYNRa+2CSD1bVqa21L69STQAAAACMaLEeRjNuXlWnJNk0OU9r7SHTKAoAAACA8Sw1MPq7JK9K8pok102vHAAAAADGttTA6NrW2iunWgkAAAAAa8K6JU73jqp6elUdXlW3nXlNtTIAAAAARrHUwGhrkt9O8rEk5/avc6ZVFAAAALB8u3btytOe9rQcd9xxedrTnpZdu3YtOv0zn/nMBafbtWtXnv70p8+5vB07duQRj3hEduzYMVjWQvPszjYtVuPeasxtX1Jg1Fq7wxyvO067OAAAAGDpTjvttJx//vn593//95x//vk5/fTTF53+M5/5zILTnXbaafnc5z435/JOOumkXH311TnppJMGy1pont3ZpsVq3FuNue1LCoyq6olzvaZdHAAAALA0u3btyllnnTUYdtZZZ83bO2XXrl05++yz01rL2WefPed0M9PMtbwdO3bkwgsvTJJceOGFOfPMM9Nay1lnnTWoY6EalrJNi9W4txp725f60Ov7TLy/RZKHJvmXJPtevAcAwE1yySWX5Dvf+U5OOOGEsUthETt27Mi677axy9inrPuvK7Njx1X+frCgHTt25IADDvie4aeddlquvfbawbBrrrkmp59+en7zN39zzumvv/76JMl1110353SnnXZarrnmmjmXd9JJJw2mnVn3Nddck9banPMs11Jq3FuNve1LvSXt+InX/0ryY0kOnG5pAACstqo6rqrOqapzLrvssrHLAWAZ3vve9w6CmiRpreU973nPvNPPhDzXXnvtnNPNXubk8mZ6F822nBoWs5Qa91Zjb/tSexjNdnWSO6xkIQAAjK+1dkqSU5Lk6KOPnkrXkiOOOCJJ8tKXvnQai2cFnXDCCTn3gq+NXcY+5fpb3Cqb73iYvx8saL4eaA972MPyjne8YxDYVFV+6qd+at7pzzzzzFx77bVZv379nNPNXubk8jZt2jRnaFRVS65hMUupcW819rYv9RlG76iqM/rXu5J8Ick/TLc0AAAAYKm2bt2a9euH/UL233//PPGJcz+CeOvWrVm3rosF9ttvvzmn27p1a/bff/85l3fiiScOpp1Z9/777z/vPMu1lBr3VmNv+5ICoyR/muTP+tcfJnlQa+15U6sKAAAAWJZDDjkkxx577GDYsccem0MOOWTe6Y855phU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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Windspeed\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot Distriubsi Kecepatan Angin (Windspeed)\")\n",
        "sns.histplot(all_df.windspeed, color = 'green')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot Kecepatan Angin (Windspeed)\")\n",
        "sns.boxplot(all_df.windspeed)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 715,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 627
        },
        "id": "Rp1rKTRVjqoK",
        "outputId": "c834cdb5-bdc3-498d-bde4-44c8ba47b4aa"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Temp\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot Distribusi Temperatur (temp)\")\n",
        "sns.histplot(all_df.temp, color='red')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot Temperatur (temp)\")\n",
        "sns.boxplot(all_df.temp)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 717,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 630
        },
        "id": "vseVy68zjqlM",
        "outputId": "812c971e-12dd-4a58-b4e7-6826df51fbc4"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Atemp\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot Distribusi suhu sebenarnya (atemp)\")\n",
        "sns.histplot(all_df.atemp)\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot suhu sebenarnya (atemp)\")\n",
        "sns.boxplot(all_df.atemp)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 718,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 630
        },
        "id": "Gh8W0Y16jqaY",
        "outputId": "c103fee1-7d9c-45e2-95cc-21a8abcb9012"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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VQMAAAAAKzfPGUbHJtma5P+tqo9U1Suq6luSHNFau2bc5vNJjphjDQAAAACs0DwDow1JHpLkf7bWHpzkS1l0+llrrSVpSz24qs6oqkuq6pKtW7fOsUwAAAAAZs0zMLoqyVWttQ+N19+SIUC6tqqOTJLx3+uWenBr7ezW2gmttRMOP/zwOZYJAAAAwKy5BUattc8n+WxV3X+86cQkn0xyfpLTxttOS/L2edUAAAAAwMptmPP+z0zy2qq6c5LLkzw9Q0j1pqp6RpIrkzxxzjUAAAAAsAJzDYxaax9NcsISd504z+MCAAAAsOvmuYYRAAAAAHshgREAAAAAHYERAAAAAB2BEQAAAAAdgREAAAAAHYERAAAAAB2BEQAAAAAdgREAAAAAHYERAAAAAB2BEQBrb7+kqlb9svHojVM/MwAAWBc2TF0AAPug25JN52xa9d1uPn3zqu8TAAD2RWYYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0BEYAQAAANARGAEAAADQERgBAAAA0FlWYFRV37ec2wAAAADY+y13htFZy7wNAAAAgL3chh3dWVWPTPK9SQ6vqufN3PWtSfafZ2EAAAAATGOHgVGSOyc5aNzubjO335zklHkVBQAAAMB0dhgYtdY+kOQDVXVOa+3KNaoJAAAAgAntbIbRgrtU1dlJjpl9TGvth+ZRFAAAAADTWW5g9OYkL0vyiiTfmF85AAAAAExtuYHRttba/5xrJQAAAADsEfZb5nbvqKpfqqojq+qQhctcKwMAAABgEssNjE5L8itJ/neSS8fLJfMqCgCA9ev666/Ps571rFx//fVTl7JuGWMAdteyAqPW2rFLXO477+IAAFh/zj333HzsYx/L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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Humidity\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot Distribusi Kelembapan (humidity)\")\n",
        "sns.histplot(all_df.hum, color = 'g')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot Kelembapan (humidity)\")\n",
        "sns.boxplot(all_df.hum)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 719,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 627
        },
        "id": "A1iE8l-moRe2",
        "outputId": "d12b2fad-7f18-46ae-e9c5-e9de465dd031"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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SwMAYKOoqtOr6qKqumjXrl2zLgdgw3rrW9+6ZDBz00035cILL0yy9Gyhr3zlK7v3nw9qWmu725rff3L9t2u+7dWCpMnjz9c4uU9rbfe65Sx1zssdv6e9SZN9MlnnSttcccUVq+6z2jksN+trXx93tTbX0sa3q3dm0mJfTXLcviwEAICNq7V2bpJzk+SEE06YyrScbdu2JUle8IIXTKP5febMM8/MxZd/dtZlsIpbDv7OHH/3ozb864kDx/wsuLvd7W55wxvecKuAZOvWrTnxxBOTJNu3b79VEHHoocN8jYc97GE5//zzF8wcaq3t3n/+srZ9EShVVVpru/9dyWT9D3vYwxacY1XtXrecpc55ueP3tDdpss8m61xpm6OPPjpXXXXVivusdg7bt2/f69rWctzV2lxLG9+u3nsmvaGqXj8+3pTkY0n+drqlAQAAwP5lx44d2br11vM2tmzZktNOG249fNZZZ91q/bOf/ezd+9/mNsN/1Q866KDdbc3vP7l+3kEHHbTg66WOv9jWrVt373fQQQfdqo2V6l98jgcddNDudctZfM6T5zb5vLe9SZN9MlnnStucddZZq+6z2jks9X2cxnFXa3MtbXy7usKkJL+f5Hnj43eT/Ehr7elTqwoAAAD2Q3e6051y8skn7/56+/btqaqcdNJJudOd7pQkOf744xfMajn00ENz//vff/f+J510UqoqJ598ck4++eQF+0+un2/7lFNO2d3e9u3bc8oppyw4/lIe8YhH3Oo4S+2zVP2Lz/Hkk0/evW45i8/5lFNO2X1uJ5988oKae9qbNNknk3WutM3xxx+/6j4rncP27dtz/PHH73VtaznuWs532rouc2utvauqjsqeG3F/YnolAQAAwP5rx44d+cQnPpGqylOf+tS88IUvvNXskbPOOitPfvKT861vfWv3rKTJ/a+44ord+0w+n1z/lKc8ZXfb119/fc4888ycddZZOfzwwzM3N5fWWn7lV34lz3ve83LzzTfnxhtvzLXXXptjjz12ybYX77NS/ZPn2Dsz5qyzzsoZZ5yRY445Zsnj7217K/VZzzY9+yx1DvP9vNba1nLc1dpcb9Vzo62qekyS/53knUkqyQ8neVpr7TVTrW4VJ5xwQrvoooum0nZV5cIdO6bS9ok7d2r7AGq752cIgLWpqotbayfMug4WmtYYbP5+Ixv9Hjfz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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Casual\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot distribusi pengguna biasa (casual)\")\n",
        "sns.histplot(all_df.casual, color = 'brown')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot pengguna biasa (casual)\")\n",
        "sns.boxplot(all_df.casual)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 720,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 627
        },
        "id": "djIWVUtVoRbr",
        "outputId": "eed902a5-df64-4918-fb31-d4ef29a212eb"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "c:\\Users\\Azhar\\anaconda3\\envs\\tf2\\lib\\site-packages\\seaborn\\_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Distribusi dan Karakteristik Variabel Registered\n",
        "plt.figure(figsize=(20,8))\n",
        "\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Plot distribusi pengguna terdaftar (registered)\")\n",
        "sns.histplot(all_df.registered, color = 'green')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.title(\"Boxplot pengguna terdaftar (registered)\")\n",
        "sns.boxplot(all_df.registered)\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 721,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 739
        },
        "id": "oWHxqF_2oRYX",
        "outputId": "eb2513d1-c84b-46ed-efe4-5d6215c686c8"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Rata-rata pengguna pertahun\n",
        "plt.figure(figsize=(20,8))\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\" Rata-rata pengguna Per-tahun\")\n",
        "all_df.groupby('year')['counts'].mean().plot.bar()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 722,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 761
        },
        "id": "4fdqp14ToRUb",
        "outputId": "a5b9a7b6-0029-4daf-9563-0b19d94a9766"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Visualisasi Rata-rata pengguna tiap musim (season)\n",
        "plt.figure(figsize=(20,8))\n",
        "plt.subplot(1,2,1)\n",
        "plt.title(\"Rata-rata pengguna tiap musim (season)\")\n",
        "all_df.groupby('season')['counts'].mean().plot.bar()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 723,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "f6oJXXSlXbrh",
        "outputId": "d8dcf363-9dea-45e5-9373-dbc4203bc3e1"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Distribusi dan kecenderungan pengguna terkait cuaca\n",
        "all_df.groupby('weathersit').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))\n",
        "plt.gca().spines['top'].set_visible(False)\n",
        "plt.gca().spines['right'].set_visible(False)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 748,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 581
        },
        "id": "86HiSd96rcE2",
        "outputId": "32875d96-d19d-4ca2-ad22-92224802ebff"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Distribusi sewa sepeda V/S hari dalam seminggu')"
            ]
          },
          "execution_count": 748,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtoAAAGDCAYAAAAVh7eRAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAwsElEQVR4nO3deZxkdX3v/9cbBgRkGZYRdRrF66AGNXGZoMYNl+tuMAkaTVRAb4i5mjGJ5qrRRFTMzaKio9lUUMQFUeOVKD+VqLgLgiCrOq2CNLIMMIMDw+LA5/fH+TbUDN0zPUOdqe6e1/Px6EefOsu3Pn3qVPW7vvU9p1JVSJIkSRqu7UZdgCRJkjQfGbQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtKVtQJJ/T/K3Q2rrPkmuT7J9u31akv81jLanuw9tXJKLkzx11HVsKMlRST46xPb+OMmXN2P9Ge+XJJVkyZZXN7u058//GHUd0rbOoC3NcS1M3JhkTZLVSb6T5BVJbn9+V9UrquptM2xro8Gkqn5RVbtW1a3DqH9U97GtS7JTO16ePMWyY5J8euD2vZNMtOnHtWPsuiTXJvl2kt/eGjVX1ceq6mlb477muvb8+dmo65C2dQZtaX54blXtBtwX+AfgdcCxw76TJAuG3aZGo6puAj4JvHRwfvsU4UXA8QOznwV8McnuwOeB9wJ7AYuBtwA3912vx56kucigLc0jVXVdVZ0M/CFwWJKHACT5cJKj2/Q+ST7fejOvTfLNJNslOQG4D/Bf7WPn/5Nk//aR+suT/AL46sC8weBz/yRnJPlVks8l2avd18GTPaGTBnvNkxyU5My23ZVJ3tXmT3Ufg228LsllrRf/x0me0uZvl+T1SX6a5JokJw3UcnyS17Tpxa39V7bb92/7Yrske7b9szLJqjY9Nt0+38JaJv++I5P8MsnlSV470Oa027blL0lySVv2xg3qOSjJd9vje3mS9yXZcZryjwf+IMkuA/OeTve/4f8bmPcs4BTgAQBV9YmqurWqbqyqL1fVudPtH2DHJB9p++eCJEsHap38G9ckuTDJ7w0sO7z1lh+T5BrgqDbvW9Pd0bD2S5JnJzm7HZeXJjlqYNnkY3dEW7Yq3SdIv53k3Nb++zZS45THfFv26HSfFqxO8sMkBw8sOy3J0W359Un+K8neST7W2vp+kv0H1r99KEy65/+/JPlC29enJ7n/wLpPa8fudUn+NcnX04aDJdk+yTuTXJ3k50lelYHnZjb4FCxDHi4kzXUGbWkeqqozgAng8VMsfk1btgjYF/ibbpN6CfALut7xXavqnwa2eSLwG3QhbCovBV4G3AtYByyfYanvAd5TVbsD9wdO2tQGSR4IvAr47daL/3Tg4rb4z4HntXrvDawC/qUt+zpw8MDf8zPgCQO3v1lVt9G9Ln6I7tOB+wA3AlMGp7tQy6QnAQcATwNeNxBYpt02yYHAvwEvacv2BgbfCNwK/CWwD/AY4CnA/56q/qr6DnA58PsDs18CfLyq1rX726Htp1OBnwC3pnvT8swke07V7gZ+FzgRWAiczPr78qd0x+gedD3jH01yr4Hlj6J7nPYF3r6xOxnmfgFuoDumFwLPBv4syfM2WOdRdI/dHwLvBt4IPBV4MPCCJE+cpu0pj/kki4EvAEfTfVrwWuAzSRYNbPvC9vctbtt+l+5Y3Qu4CHjzNPc5ue1bgD2Bcdr+TLIP8GngDXT77MfA7wxs9yfAM4GHAY+gOy4lzZBBW5q/fkn3D3hDv6YLxPetql9X1TerqjbR1lFVdUNV3TjN8hOq6vyqugH4W7qgMZMTGX8NLEmyT1VdX1Xfm8E2twJ3Aw5MskNVXVxVP23LXgG8saomqupm4Cjg0Nb79nXgcenGrj8B+CfgsW27J7blVNU1VfWZqlpbVWvoAsl0oWlLa5n0lrZfz6MLTC+awbaHAp+vqm+0ZX8L3DbZYFWdVVXfq6p1VXUx8B8bqR/gI7ThI+mGhhzC+sNGngD8sKrWVNWvgMcBBXwAWJnk5CT7bqT9b1XVKW28/QnAbw3U+qmq+mVV3VZVnwRWAAcNbPvLqnpv+1umO/YmDW2/VNVpVXVeq+tc4BNTrPu2qrqpqr5MF8w/UVVXVdVlwDeBh09T53TH/IuBU9q+uq2qTgXOpPs0YdKHquqnVXUd3ScOP62q/25vij61kfsE+GxVndHW/RhdcKa1f0FV/Wdbthy4YmC7F9C9MZioqlV0Q9MkzZBBW5q/FgPXTjH/n+l6tL6c5GdJXj+Dti7djOWXADvQ9RxuysvphiP8qH30/ZxNbVBV48Bf0IXPq5KcmOTebfF9gc+2j95X0/Xy3Qrs2wLwDXQB4/F0Y41/2Xqlbw/aSXZJ8h9tCMKvgG8AC6d647CltQw0seF+m8m29x7crr25uWbydpIHpBvuckWr/+/Z+GNxAvCkVvehdOHt7IHlk8NGJu/voqo6vKrGgIe0et69kfYHQ9taYKeBYQcvTXLOwN/5kA1q3dRxN2ho+yXJo5J8Ld3woevo3vhsuO6VA9M3TnF712nqnO6Yvy/w/Ml90fbH4+jeFN/V+4Q7Pw6T626434ruEy+mWs7mPSbSNs+gLc1D6a4CsRi403jW1jP5mqr6H3Qf6/9V2rhiup7KqWyqx3u/gen70PXaXU0XbG8f/9vC6u0fhVfViqp6EXAP4B+BTye5+ybui6r6eFU9ji6cVNsWuhDwzKpaOPCzU+tlhC5MHwrs2OZ9HTiM7uP0c9o6rwEeCDyqfbw/ObwkQ64F7rzffjmDbS8f3C7d+Oq9B9r5N+BHwAGt/r+ZrvZW/yV0PbAvphuWcPwGq6wXtDfY9kfAh+kC8mZJcl+6XvFXAXtX1ULg/A1q3dRxN2iY++XjdMNc9quqPYB/38i6m2Ujx/yldJ8MDT7md6+qvnuQL2dgiE2SsP6Qm8s3uD14zMIGz3HgnsMuUJrLDNrSPJJk99ZDdiLw0TYkYcN1npNkSfuHeh1dT+nkR+xXAlty7d0XJzmwhZu3Ap9uQwV+QteD+ew21vdNdEMtJmt5cZJF1Y2NXt1m38ZGJHlgkicnuRtwE11P3uQ2/w68vYU4kixKcsjA5l+nC3bfaLdPa7e/VXdcSnC31ubqdCcgTjvu9S7WAvC3rQf9wcARdFcB2dS2nwaek+4yezvS7e/B1/LdgF8B1yd5EPBn09U/4Pi2Hx5LN6xg8u+7H3C3qrqo3X5QkteknRyaZD+64S4zGfKzobvTBemVra0j2ILAPmCY+2U34NqquinJQcAf3YW61rORY/6jwHOTPD3dCYg7pTuZeNoTcYfkC8BDkzyvfdLwStYPyycBr053AvFCuisaDToHeGGSHdKd6Hpoz/VKc4pBW5of/ivJGrpesTcC76ILblM5APhv4Hq6k6n+taq+1pb9X+BN7aPr106z/VROoOvZvALYCVgG3VVQ6E44+yBwGV3v1+DH0s8ALkhyPd1JYi+cwVjcu9GNE7263d896E7korVxMt2wmDV0AfBRA9t+nS5ETQbtb9H1xn1jYJ13Azu39r8HfLGnWibrGQe+Aryjjffd6LZVdQFdGPo4XW/jKtbfp6+lC4Zr6HqMP8mmfYZuPP9XqurygfnPZv3e7DWtjtOT3NDqOp/uU4DNUlUXAu+kOwavBB4KfHtz2xlob5j75X8Db237/u+YwUm6m2HKY76qLqUbH/83dG8+LgX+mp7/T1fV1cDz6c5ZuAY4kG5s+OQlGz8AfBk4Fzib7nhYR/cGHbqx8Pen299vodv/kprUJs+BkiQNU7rLsP0c2KGdgDYrJTkFeF9VTTl0RPNPupOFJ4A/HngDPrj8mcC/V9V9t3px0hxkj7YkaTqnAXcKW5pf2nCVhW0I1OTY9e+1ZTsneVaSBekuQfhm4LMjLFeaUwzakqQpVdU/zWAoj+a+x9Bd0/xq4LnA8wYe99ANCVlFN3TkIrrhNJJmwKEjkiRJUg/s0ZYkSZJ6YNCWJEmSerBg06vMPfvss0/tv//+oy5DkiRJ89xZZ511dVUtmmrZvAza+++/P2eeeeaoy5AkSdI8l+SS6ZY5dESSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6sGCURcwHyxfvpzx8fGhtDUxMQHA2NjYUNpbsmQJy5YtG0pbkiRJmjmD9ixz4403jroESZIkDYFBewiG2WM82dby5cuH1qYkSZK2PsdoS5IkST0waEuSJEk9MGhLkiRJPTBoS5IkST0waEuSJEk9MGhLkiRJPTBoS5IkST0waEuSJEk9MGhLkiRJPfCbISVJkjRjy5cvZ3x8fChtTUxMADA2NjaU9pYsWTLUb+y+qwzakiRJGokbb7xx1CX0yqAtSZKkGRtmj/FkW8uXLx9am7OJY7QlSZKkHhi0JUmSpB44dERznidlSJKk2cigLQ2Y7ydlSJKkrcegrTnPkzIkjYKfpknaFIO2JEkj5qdp0vxk0JYkaQv4aZqkTen1qiNJ/jLJBUnOT/KJJDsluV+S05OMJ/lkkh3bundrt8fb8v0H2nlDm//jJE/vs2ZJkiRpGHoL2kkWA8uApVX1EGB74IXAPwLHVNUSYBXw8rbJy4FVbf4xbT2SHNi2ezDwDOBfk2zfV92SJEnSMPR9He0FwM5JFgC7AJcDTwY+3ZYfDzyvTR/SbtOWPyVJ2vwTq+rmqvo5MA4c1HPdkiRJ0l3SW9CuqsuAdwC/oAvY1wFnAaural1bbQJY3KYXA5e2bde19fcenD/FNpIkSdKs1OfQkT3peqPvB9wbuDvd0I++7u/IJGcmOXPlypV93Y0kSZI0I30OHXkq8POqWllVvwb+E3gssLANJQEYAy5r05cB+wG05XsA1wzOn2Kb21XV+6tqaVUtXbRoUR9/jyRJkjRjfQbtXwCPTrJLG2v9FOBC4GvAoW2dw4DPtemT223a8q9WVbX5L2xXJbkfcABwRo91S5IkSXdZb9fRrqrTk3wa+AGwDjgbeD/wBeDEJEe3ece2TY4FTkgyDlxLd6URquqCJCfRhfR1wCur6ta+6pYkSZKGodcvrKmqNwNv3mD2z5jiqiFVdRPw/GnaeTvw9qEXKEmSJPWk78v7SZIkSdskv4JdkiTNKcuXL2d8fHwobU1MTAAwNjY2lPYAlixZwrJly4bWnuYug7YkzVGzOWwYNDRX3HjjjaMuQfOYQVuSZNjQnDLMN3GTbS1fvnxobUqTDNqSNEcZNiRpdvNkSEmSJKkHBm1JkiSpBwZtSZIkqQcGbUmSJKkHBm1JkiSpB151RNIWm83XcQav5SxJGi2DtqRZwes4S5LmG4O2pC3mdZwlSZqeY7QlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeGLQlSZKkHhi0JUmSpB4YtCVJkqQeLBh1AZIkaf5bvnw54+Pjoy7jTlasWAHAsmXLRlzJ1JYsWTJra9OmGbQlSVLvxsfHOf+HP2S3HWdX9Fi37lYALrnoghFXcmdrblk36hJ0F82uo12SJM1bu+24gIP23XPUZcwZZ1y5atQl6C5yjLYkSZLUA3u0JUnbDMcJbz7HCEtbbpsN2r7Ybj5fbCXNdePj41xw3kUs3OUeoy5lPbfdEgAu++k1I65kfavXXjXqEqQ5bZsN2uPj45x93oXctsteoy5lPbmlADjrp1eMuJL1bbf22lGXIElDsXCXe/CkB71w1GXMCV/70YmjLkGa07bZoA1w2y57cdOBzxl1GXPCThd+ftQlSJIkzSm9ngyZZGGSTyf5UZKLkjwmyV5JTk2yov3es62bJMuTjCc5N8kjBto5rK2/IslhfdYsSZIkDUPfVx15D/DFqnoQ8FvARcDrga9U1QHAV9ptgGcCB7SfI4F/A0iyF/Bm4FHAQcCbJ8O5JEmSNFv1FrST7AE8ATgWoKpuqarVwCHA8W2144HntelDgI9U53vAwiT3Ap4OnFpV11bVKuBU4Bl91S1JkiQNQ5892vcDVgIfSnJ2kg8muTuwb1Vd3ta5Ati3TS8GLh3YfqLNm27+epIcmeTMJGeuXLlyyH+KJEmStHn6DNoLgEcA/1ZVDwdu4I5hIgBUVQE1jDurqvdX1dKqWrpo0aJhNClJkiRtsT6vOjIBTFTV6e32p+mC9pVJ7lVVl7ehIZMX6bwM2G9g+7E27zLg4A3mn9Zj3ZIkSfOK3x+y+Ybx/SG9Be2quiLJpUkeWFU/Bp4CXNh+DgP+of3+XNvkZOBVSU6kO/HxuhbGvwT8/cAJkE8D3tBX3dJ854vtlvELmyTNZePj4/z4/IvYb7d7jrqU9eywrhtcsfaSVSOuZH2XrhnO95n0fR3tPwc+lmRH4GfAEXTDVU5K8nLgEuAFbd1TgGcB48Dati5VdW2StwHfb+u9tar89hRpC42Pj3P2BWfDwlFXsoHbul9nX3b2aOuYyupRFyBJd91+u92T1xx0xKjLmBPeecaHhtJOr0G7qs4Blk6x6ClTrFvAK6dp5zjguKEWJ23LFsJtB9826irmjO1O6/tKqJKk+cj/HpIkSVIPtumvYJekrc0x8pvP8fGS5iqDtiRtRePj4/zonHOYXacj3fHx5upzzhllGXcynNORJGk0DNqStJXdE3g5GXUZc8Kxw/mqBUkaCcdoS5IkST0waEuSJEk9MGhLkiRJPTBoS5IkST0waEuSJEk9MGhLkiRJPTBoS5IkST3wOtoaCb8db/P57XiSJM0tBm2NxPj4OD85/wfcZ9dbR13Kenb8dfchz00Xf3/ElazvF9dvP+oSJEnSZjJoa2Tus+utvGnp9aMuY044+sxdR12CJEnaTI7RliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknowo6Cd5NVJdk/n2CQ/SPK0vouTJEmS5qoFM1zvZVX1niRPB/YEXgKcAHy5t8okSdK8MTExwZpb1nHGlatGXcqcseaWdUxMTIy6DN0FMx06kvb7WcAJVXXBwDxJkiRJG5hpj/ZZSb4M3A94Q5LdgNv6K0uSpOGbmJjgurVr+NqPThx1KXPC6rVXURM3DqWtsbExbl1zHQftu+dQ2tsWnHHlKsbGxkZdhu6CmQbtlwMPA35WVWuT7A0c0VtVkiRJ0hw306B9alU9ZfJGVV2T5CTgKRvZRpKkWWVsbIzcfA1PetALR13KnPC1H53I4rG9R12GhmBiYoIb1qzhnWd8aNSlzAmXrrmCu0/ccJfb2WjQTrITsAuwT5I9uWNc9u7A4rt875K0jZmYmGANcCw16lLmhMuB6z0ZTNIctake7T8F/gK4N3AWdwTtXwHv668sSZIkDcvY2Bhrb13Faw5y5O9MvPOMD7HL2F0/n2CjQbuq3gO8J8mfV9V77/K9zSITExNst/Y6drrw86MuZU7Ybu01TEysG3UZ0pw3NjbG6quv5uVeuGlGjqVY6MlgkuaoGY3Rrqr3JvkdYP/BbarqIz3VJUmSJM1pMwraSU4A7g+cA9zaZhcwZ4P22NgYV968gJsOfM6oS5kTdrrw84yN3XPUZUiSJM0ZM73qyFLgwKry7B1JkiRpBmb6zZDnA3ZnSpIkSTM00x7tfYALk5wB3Dw5s6p+t5eqJPVmYmICroPtTpvp+2yxGibKS8xJkjbPTIP2UX0WoW1Pd+H87Tn6zF1HXcqccMma7bm71xKWJGlOmelVR77edyGSto6xsTFWZiW3HXzbqEuZM7Y7bTvGFnuJOUnS5pnpVUfWwO1fY7YjsANwQ1Xt3ldhmt/Gxsa4ad3lvGnp9aMuZU44+sxd2clrCUuSNKfMtEd7t8npJAEOAR7dV1GSJEnSXLfZZ0NV5/8BTx9+OZIkSdL8MNOhI78/cHM7uutq39RLRZIkSdI8MNOrjjx3YHodcDHd8BFJkiRJU5jpGO0j+i5EkiRJmk9mNEY7yViSzya5qv18JomXQJAkSZKmMdOTIT8EnAzcu/38V5u3SUm2T3J2ks+32/dLcnqS8SSfTLJjm3+3dnu8Ld9/oI03tPk/TuJJmJIkSZr1Zhq0F1XVh6pqXfv5MLBohtu+Grho4PY/AsdU1RJgFfDyNv/lwKo2/5i2HkkOBF4IPBh4BvCvSbaf4X1LkiRJIzHToH1Nkhe33untk7wYuGZTG7XhJc8GPthuB3gy8Om2yvHA89r0Ie02bflTBq7ZfWJV3VxVPwfGgYNmWLckSZI0EjMN2i8DXgBcAVwOHAocPoPt3g38H2Dyu573BlZX1bp2ewJY3KYXA5cCtOXXtfVvnz/FNrdLcmSSM5OcuXLlyhn+WZIkSVI/Zhq03wocVlWLquoedMH7LRvbIMlzgKuq6qy7WOOMVNX7q2ppVS1dtGimo1okSZKkfsz0Otq/WVWrJm9U1bVJHr6JbR4L/G6SZwE7AbsD7wEWJlnQeq3HgMva+pcB+wETSRYAe9ANT5mcP2lwG0mSJGlWmmmP9nZJ9py8kWQvNhHSq+oNVTVWVfvTncz41ar6Y+BrdENPAA4DPtemT263acu/WlXV5r+wXZXkfsABwBkzrFuSJEkaiZn2aL8T+G6ST7XbzwfevoX3+TrgxCRHA2cDx7b5xwInJBkHrqUL51TVBUlOAi6k+1bKV1bVrVt435IkSdJWMdNvhvxIkjPprhgC8PtVdeFM76SqTgNOa9M/Y4qrhlTVTXQBfqrt386WB3tJkiRpq5tpjzYtWM84XEuSJEnbspmO0ZYkSZK0GQzakiRJUg8M2pIkSVIPDNqSJElSDwzakiRJUg8M2pIkSVIPDNqSJElSD2Z8HW1J0nBcARxLjbqM9VzTfu890iru7Apg4aiLkKQtZNCWpK1oyZIloy5hSitXrABg4QEHjLiS9S1k9u4zSdoUg7YkbUXLli0bdQlTmqxr+fLlI65EkuYPx2hLkiRJPTBoS5IkST0waEuSJEk9cIy2JEnSNuDSNVfwzjM+NOoy1nPV2msBuMcue424kvVduuYKHsied7kdg7YkSdI8N1uv3vPrFVcDsMt973qoHaYHsudQ9plBW5IkaZ7zikejYdCWtkWrYbvTZtkpGte337uOtIqprQYWj7oISdJcY9CWtjGz9ePDFe0LUw5YPLu+MAWAxbN3v0lzyZpb1nHGlatGXcZ61q67FYBdFmw/4krubM0t60Zdgu4ig7a0jfHjQ0mjMFvfrE6+yb/vLPtW1Emzdb9pZgzakiSpd77J17Zolg3SlCRJkuYHg7YkSZLUA4O2JEmS1AODtiRJktQDg7YkSZLUA4O2JEmS1AODtiRJktQDg7YkSZLUA4O2JEmS1AO/GVIj84vrt+foM3cddRnruXJt995z311uG3El6/vF9dvzgFEXIUmSNotBWyOxZMmSUZcwpVtWrABgp/0PGHEl63sAs3efSZKkqRm0NRLLli0bdQlTmqxr+fLlI65EkiTNdY7RliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknqwTZ8Mud3aa9npws+Puoz15KZfAVA77T7iSta33dprgXuOugxJkqQ5Y5sN2rP1UmkrVqwB4ID7z7ZQe89Zu88kSZJmo202aHt5OUnaNq1eexVf+9GJoy5jPdfftAqAXXfac8SVrG/12qtYzN6jLkOas7bZoC1J2vbM1k/mVqy4FoDF959doXYxe8/afSbNBQZtSdI2w08zJW1NXnVEkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSepBb0E7yX5JvpbkwiQXJHl1m79XklOTrGi/92zzk2R5kvEk5yZ5xEBbh7X1VyQ5rK+aJUmSpGHps0d7HfCaqjoQeDTwyiQHAq8HvlJVBwBfabcBngkc0H6OBP4NumAOvBl4FHAQ8ObJcC5JkiTNVr0F7aq6vKp+0KbXABcBi4FDgOPbascDz2vThwAfqc73gIVJ7gU8HTi1qq6tqlXAqcAz+qpbkiRJGoatMkY7yf7Aw4HTgX2r6vK26Apg3za9GLh0YLOJNm+6+Rvex5FJzkxy5sqVK4f7B0iSJEmbqfegnWRX4DPAX1TVrwaXVVUBNYz7qar3V9XSqlq6aNGiYTQpSZIkbbFeg3aSHehC9seq6j/b7CvbkBDa76va/MuA/QY2H2vzppsvSZIkzVp9XnUkwLHARVX1roFFJwOTVw45DPjcwPyXtquPPBq4rg0x+RLwtCR7tpMgn9bmSZIkSbPWgh7bfizwEuC8JOe0eX8D/ANwUpKXA5cAL2jLTgGeBYwDa4EjAKrq2iRvA77f1ntrVV3bY92SJEnSXdZb0K6qbwGZZvFTpli/gFdO09ZxwHHDq06SJEnql98MKUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPXAoC1JkiT1wKAtSZIk9cCgLUmSJPVgwagLkCRJ0tyxfPlyxsfHh9LWihUrAFi2bNlQ2luyZMnQ2hoGg7YkSZJGYueddx51Cb0yaEuSJGnGZlOP8WznGG1JkiSpBwZtSZIkqQcGbUmSJKkHBm1JkiSpBwZtSZIkqQcGbUmSJKkHBm1JkiSpBwZtSZIkqQcGbUmSJKkHBm1JkiSpBwZtSZIkqQcGbUmSJKkHBm1JkiSpBwtGXYAkacssX76c8fHxobS1YsUKAJYtWzaU9pYsWTK0tiRprjJoS5LYeeedR12CJM07Bu0hsFdJ0ij43Jak2c2gPcvYq7T5fKMjSZJmI4P2EBik5g/f6EiSpGExaGvO842OJEmajby8nyRJktQDg7YkSZLUA4O2JEmS1APHaEuStAW84tHozOZ9D/N//2vmDNqSJI2YVzwaHfe9+mTQliRpC9hjOTrue80VjtGWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6YNCWJEmSemDQliRJknpg0JYkSZJ6MGeCdpJnJPlxkvEkrx91PZIkSdLGzImgnWR74F+AZwIHAi9KcuBoq5IkSZKmt2DUBczQQcB4Vf0MIMmJwCHAhSOtStrGLV++nPHx8aG0tWLFCgCWLVs2lPYAlixZMtT2JEnaHHOiRxtYDFw6cHuizZM0T+y8887svPPOoy5DkqShmSs92puU5EjgSID73Oc+I65G2jbYWyxJ0vTmSo/2ZcB+A7fH2rzbVdX7q2ppVS1dtGjRVi1OkiRJ2tBcCdrfBw5Icr8kOwIvBE4ecU2SJEnStObE0JGqWpfkVcCXgO2B46rqghGXJUmSJE1rTgRtgKo6BThl1HVIkiRJMzFXho5IkiRJc4pBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqgUFbkiRJ6oFBW5IkSeqBQVuSJEnqQapq1DUMXZKVwCWjruMu2Ae4etRFbMPc/6Pjvh8t9/9ouf9Hx30/WnN9/9+3qhZNtWBeBu25LsmZVbV01HVsq9z/o+O+Hy33/2i5/0fHfT9a83n/O3REkiRJ6oFBW5IkSeqBQXt2ev+oC9jGuf9Hx30/Wu7/0XL/j477frTm7f53jLYkSZLUA3u0JUmSpB4YtIcsyRuTXJDk3CTnJHnUENo8Kslrh1HffJWkknx04PaCJCuTfH5I7fsYTCHJ3u04PyfJFUkuG7i94xDv5+BhPZZzSZJjkvzFwO0vJfngwO13JvmrGbSzf5Lzeypz8j6u77P92WAjx/vqJBduhfs/PMn7+r6fuSzJrQOP0TlJ9p9inVOSLJxivq/zM7A5Oacds/cewn1enGSfu9rOKCwYdQHzSZLHAM8BHlFVN7eDYmhhQxt1A/CQJDtX1Y3A/wQuG3FN815VXQM8DLp/UsD1VfWOUdY0z3wbeAHw7iTb0V1rdveB5b8D/OUoCtsWTXe8tzC3xW8EkyyoqnXDqFHcWFUPm2pBktANmX3W1i1p/tiCnHM4cD7wy824j3n1fLBHe7juBVxdVTcDVNXVVfXLwXdiSZYmOa1NH5XkuCSnJflZkmWTDbV3jD9J8i3ggQPz/yTJ95P8MMlnkuySZLckP0+yQ1tn98Hb25BTgGe36RcBn5hckGSvJP+vvQP/XpLfbPN9DIYsyYeTHDpw+/qB6b9u++7cJG9p8+6e5Attf56f5A/b/Gck+VGSHwC/P9DGQUm+m+TsJN9J8sA2/xtJHjaw3reS/Fb/f3GvvgM8pk0/mO4f1pokeya5G/AbQCX5epKzWo/3vQCSPLLt0x8Cr5xssPUw/WeSLyZZkeSfBpY9re3bHyT5VJJd2/x/SHJhe9ze0ebdr617XpKjB9rYNclXWhvnJTmkzX9r1u+df3uSV/ez20Zi+yQfSNfT9+UkOwO015albXqfJBe36cOTnJzkq8BXktyrHcPntOfB49t6R7TXoTOAx07eWZLnJjm9PQ/+O8m+SbZrj+mits52ScYnb2+L0n2a8+MkH6F7/uyX9f8n+zq/eabLOX/X9tf5Sd6fzqHAUuBj7bjeORvPQyck+TZwQrpPj77cnk8fBDJZQLr/5We1ZUe2eS9L8u6Bdf4kyTFbaZ9sXFX5M6QfYFfgHOAnwL8CT2zzLwb2adNLgdPa9FF0/0jvRtdTdQ2wA/BI4DxgF7req3HgtW2bvQfu72jgz9v0h4DntekjgXeOen9s5X1/PfCbwKeBndrjcDDw+bb8vcCb2/STgXN8DIb+GBwFvBb4MHDo4GPTfj+N7szy0L3J/zzwBOAPgA8MrL9HewwvBQ5o65808FjuDixo008FPtOmDwPe3aYfAJw56n0ypP36c+A+wJ8CrwDeBjyLLnR9tx2/i9q6fwgc16bPBZ7Qpv8ZOL9NHw78bGA/XwLs147/bwB3b+u9Dvg7YG/gx9xx8vzC9vtk4KVt+pUDj/MCYPc2vU977gTYH/hBm78d8NPB59Jc+5k83tv0/sA64GHt9knAi9v0acDSgf1x8cDjMAHs1W6/Bnhjm94e2I0u1PwCWETXa/ht4H1tnT0HHpP/RXu9Ad4M/MXAc+4zo95XW/lxuZXu9f8c4LPtsbkNePTAOhe3x8LX+c3fv9PlnL0G1jkBeG6bvv34H9z3bXrDPHQWsHO7vRz4uzb9bKAGtpt8zuxM9+Zp71bXT4Ed2rLvAA8d9f6qKnu0h6mqrqd74h4JrAQ+meTwTWz2haq6uaquBq4C9gUeD3y2qtZW1a/o/qFNekiSbyY5D/hjul4ugA8CR7TpI+heDLYpVXUu3Yvqi+h6twc9ju7JT1V9Fdg7yeRH8D4GW8fT2s/ZwA+AB9EF6fOA/5nkH5M8vqqua8t+XlUrqnvV/OhAO3sAn0o35vgY7tj/nwKe03qXXkYX+OeD79ANEfkdumD93YHblwEPAU5Ncg7wJmAs3fjThVX1jdbGCRu0+ZWquq6qbgIuBO4LPBo4EPh2a+uwNv864Cbg2CS/D6xtbTyWOz41Gmw/wN8nORf4b2AxsG9VXQxck+ThtOOguqEY88XPq+qcNn0W3WvRppxaVde26e8DR6QbkvLQqloDPIouiKysqluATw5sOwZ8qb0O/TV3PA+OA17apl/Gtvc6dGNVPaz9/F6bd0lVfW+KdX2d30wbyTlPap+wnEfXmfXg6VuZ1snVDf2ErhPmo+0+vwCsGlhvWbpP6r5H10lwQKvrq3T/Ax5EF7jP24Iahs4x2kNWVbfSvYM7rR1wh9H1dEy+qdlpg01uHpi+lU0/Jh+mezf9w3ZwH9zu99vtI7KDge2rqtcTn2axk4F30O2XvWe4jY/BcN1+vKcbVzw5fi/A/62q/9hwgySPoOulPTrJV1j/H96G3gZ8rap+L93Y2NMAqmptklOBQ+jGNT9yKH/N6H2bLlQ/lK735lK63s9f0f3ti6vqMYMbZIoTvTYw1TEfuuD3og1XTnIQ8BTgUOBVdP9Ioetl2tAf0/XAPrKqft2GSky+7n2Qrif3nnSBcD7ZcJ/u3KY39vp/w+REVX0jyRPoeu8+nORddI/xdN4LvKuqTm6vOUe1di5NcmWSJwMH0T0e27obNr3KnXwYX+enNEXO+VO6T5SXtuPvKO58rE+a0fNhOm2/PxV4THvNP431X1/+BvgRs+gNkD3aQ5TkgUkOGJj1MLqPZS/mjn/6fzCDpr4BPK+NZ9oNeO7Ast2Ay1uv3YYvoB8BPs4sOsBG4DjgLVO8k/0mbX+1J+rVrQdjOj4GW+5i7jjef5duKA7Al4CX5Y5xv4uT3CPdGelrq+qjdEMcHkH3Qrl/kvu3bQfD3x7ccaLr4Rvc9wfpPnL8flWtYn74Dt3JR9dW1a2tB3Qh3djtTwCL0p2gRJIdkjy4qlYDq5M8rrUxk7D1PeCxSZa0tu6e5AHt8dqjqk6hO/Fyctz7t4EXTtH+HsBVLWQ/ia5XfNJngWcAv013PGwLLuaO58Oh062U5L7AlVX1Abrj+BHA6cAT23jVHYDnD2wy+Dw4bIPmPkjXG/ipFoo0NV/nN9M0OefHbfrq9noxeJyvoduXky5mZnnoG8Aftft8Jt1QKeiO+1UtZD+I7pM4AKrqdLoe7j9i4BytUbNHe7h2Bd7bepPW0Y33OpLuhKVjk7yN1vu2MVX1gySfBH5IN5Th+wOL/5buxXdl+z14AH+MbizZrDnAtraqmqALWhs6CjiufZy9ljv/Y9qwHR+DLfcB4HPto70v0nopqurLSX4D+G4S6MbVvxhYAvxzktuAXwN/VlU3tZNcvpBkLd0bpcn9/E/A8UneBHxh8I6r6qwkv2J+/QM8j2486cc3mLdrVV2V7oSj5Un2oHtNfzdwAd3H2sclKeDLm7qTqlrZeu4+ke5ES+iGoqyhezx3ouv1nryc4KuBjyd5HfC5gaY+BvxX6+k6k+5N0+R93JLka8DqbSgAvgM4afJ43sh6BwN/neTXdM+Nl1bV5a138LvAarqxsZOOohtCtYruI/P7DSw7me45MJ+eB0Pn6/wWmS7nrKb7xO0K1t+PHwb+PcmNdJ0Db2FmeegtdK9FF9B1Nvyizf8i8IokF9EF/A2HBJ1Ed67ErOlo8Zsh55H2D/eQqnrJqGvZVvkYjFbrHT8NeFBV3TbicrSBNpToB8Dzq2rFqOuZr9Jd5eSYqnr8qGuZj3ydn73Sfd/CMVX1lVHXMske7XkiyXuBZ9KNc9UI+BiMVpKXAm8H/sqQPfskOZDuSjOfNWT3J8nrgT/Dsdm98HV+dmo97GcAP5xNIRvs0ZYkSZJ64cmQkiRJUg8M2pIkSVIPDNqSJElSDwzakrSNS3Jau1LFxtY5PMn7tlZNkjQfGLQlSZKkHhi0JWmOSfLXSZa16WOSfLVNPznJx5I8Lcl3k/wgyacGvo3zkUm+nuSsJF9Kcq8N2t0uyYeTHN1uH5HkJ0nOAB47sN5zk5ye5Owk/51k37btiiSLBtoan7wtSdsig7YkzT3fBCa/jGQpsGv7qujHA+fSfaPjU6vqEXTfzvhXbfl7gUOr6pHAcXTXHZ+0gO4b71ZU1ZtaCH8LXcB+HHDgwLrfAh5dVQ8HTgT+T7t2+Ue54/rNT6W7pu3K4f7pkjR3+IU1kjT3nAU8MsnuwM1037a4lC5on0wXir/dvup+R7qv8H4g8BDg1DZ/e+DygTb/AzipqibD96OA0yaDcvuq6ge0ZWPAJ1sY3xH4eZt/HN3Xsb8beBl+BbikbZxBW5LmmKr6dZKfA4cD36HrxX4SsIQu9J5aVS8a3CbJQ4ELquox0zT7HeBJSd5ZVTdtooT3Au+qqpOTHAwc1eq6NMmVSZ4MHITfTihpG+fQEUmam74JvBb4Rpt+BXA28D3gsUmWACS5e5IHAD8GFiV5TJu/Q5IHD7R3LHAKcFKSBcDpwBOT7N2GnTx/YN09gMva9GEb1PVBuiEkn6qqW4f210rSHGTQlqS56ZvAvYDvVtWVwE3AN9tQj8OBTyQ5l27YyIOq6hbgUOAfk/wQOAf4ncEGq+pddGH9BOBKup7q7wLfBi4aWPUo4FNJzgKu3qCuk4FdcdiIJJGqGnUNkqR5ol2P+5iqevwmV5akec4x2pKkoUjyeuDPcGy2JAH2aEuSJEm9cIy2JEmS1AODtiRJktQDg7YkSZLUA4O2JEmS1AODtiRJktQDg7YkSZLUg/8fHWIDY+k8kpAAAAAASUVORK5CYII=",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Dsitribusi sewa perhari\n",
        "plt.figure(figsize=(12,6))\n",
        "sns.boxplot(x='weekday', y='counts', data=all_df)\n",
        "plt.title('Distribusi sewa sepeda V/S hari dalam seminggu')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 725,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "zlzJUsQsOuTK",
        "outputId": "7d8d216f-fe2b-4a8e-cca7-89b30a4918a3"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Distribusi sewa sepeda perbulan\n",
        "plt.figure(figsize=(12,6))\n",
        "sns.boxplot(x='month', y='counts', data=all_df)\n",
        "plt.title('Distribusi sewa sepeda V/S dalam sebulan')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 726,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "FwlkfmhPPpRB",
        "outputId": "64a8f72e-7139-4d42-f3f4-d0c075e690b8"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Distribusi sewa sepeda permusim\n",
        "hour_df['season'] = hour_df[['season_1', 'season_2', 'season_3', 'season_4']].idxmax(axis=1)\n",
        "hour_df['season'] = hour_df['season'].map({'season_1': 'spring', 'season_2': 'summer', 'season_3': 'fall', 'season_4': 'winter'})\n",
        "plt.figure(figsize=(12,6))\n",
        "sns.boxplot(x='season', y='counts', data=all_df)\n",
        "plt.title('Distribusi sewa sepeda V/S seasons')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 727,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "a-RFBUZNQTq6",
        "outputId": "9740cbaa-e386-4852-cc4f-5a2e55c62f4e"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Hubungan antara kondisi cuaca dengan persewaan sepeda\n",
        "plt.figure(figsize=(12,6))\n",
        "sns.boxplot(x='weathersit', y='counts', data=all_df)\n",
        "plt.title('Hubungan antara kondisi cuaca  V/S persewaan sepeda')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 733,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 490
        },
        "id": "3tV8o-IXQXGi",
        "outputId": "ddd8e901-3520-448f-ba07-b23376da06cd"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Hubungan antara kondisi suhu pada persewaan sepeda\n",
        "plt.figure(figsize=(20,6))\n",
        "sns.boxplot(x='temp', y='counts', data=all_df)\n",
        "plt.title('Hubungan antara kondisi suhu V/S persewaan sepeda')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 729,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 490
        },
        "id": "qkntq9cWQs0-",
        "outputId": "4c4009a5-c11e-47af-b9dd-faaa2d348332"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Hubungan antara kondisi suhu sebenarnya pada persewaan sepeda \n",
        "plt.figure(figsize=(20,6))\n",
        "sns.boxplot(x='atemp', y='counts', data=hour_df)\n",
        "plt.title('Hubungan antara kondisi suhu sebenarnya V/S persewaan sepeda')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 734,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 490
        },
        "id": "DkR9fqYUQ5vy",
        "outputId": "bff6be36-d9cc-45b3-e330-1c29aee2d704"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Hubungan antara kondisi kelembaban pada persewaan sepeda\n",
        "plt.figure(figsize=(20,6))\n",
        "sns.boxplot(x='hum', y='counts', data=all_df)\n",
        "plt.title('Hubungan antara kondisi kelembaban V/S persewaan sepeda')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 735,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 490
        },
        "id": "VMqF94VkRHYX",
        "outputId": "c419fc2d-50ba-41a2-db41-4b9372455e58"
      },
      "outputs": [
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABM8AAAGDCAYAAAA8tTd+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABWUElEQVR4nO3dfbwcd133//cnaVJOT8v2JmmbTdsUTgva1IoSQcFcF7YaocrVBA3WogLir3pAgUuPFzeXCiJ4oVcUq+ByVQG5LxRtqF4IQXMVDsqNLdTQgEi3tLTdtnCa5KTdbJs2+f7+mJmTOZvdc/ZmZr5z83o+HudxZndnZ787Ozff+czn+/2ac04AAAAAAAAAjrfCdwEAAAAAAACAvCJ4BgAAAAAAAPRB8AwAAAAAAADog+AZAAAAAAAA0AfBMwAAAAAAAKAPgmcAAAAAAABAHwTPAAAYkJk9x8zu8V2OqjEzZ2YX+C5HmZnZ683sr32XA8ViZnea2Y/7LgcAAGkjeAYAqIxeF3pm9hIz+5yvMhWNmf2Nmb3ZdznyqqiBPufcHzrnfmXY95nZa83ssz2eX2Nmh83s4thz/8fMrjaz1Wb2J2Z2j5k9HO6XfzbmVwAAAEgNwTMAAJAZMzvBdxmQqA9IepaZPanr+SslfdU5d1vsuedJ+oSk10naJOkZkk6R9BxJX067oGx7AABgVATPAACI6c4c6pVpFTZxmwszZl4Ue/4mM/uV2ONFWW3hsn/NzL5pZgfM7B1mZuFrK8NsnDkz+5aZ/Xo4/wnh6y81s6+b2UNmdoeZ/Wpsuc8Js3h+y8y+Y2b3mdlLl/iOIy3LzK6W9CJJ/yPMGPr78PnXmlkzXN7XzGxb1zr4FzN7m5k9KOmNZjZlZrvN7MHw+37QzE4d8Pf5UTO728yeEz7+5fC77DezT5nZhti8G83s02a2z8weMLPXh8+viJX5QTP7qJmdHr52frjerzazVvj9Z2LLfIaZfT78/e4zs7eb2erwtSgD69/D9fNzZnaamf2DmX03LOM/mNk5seXdZGZ/EK6jh8xsl5mt6fPdx1qWmf2Smd0VfufftVgmppm90cw+0LUOXmxm3w5/o//Zq0zOuXsk7Zb0i10v/ZKk98U++xJJB8L5f0jSDc65lgvc6Zx7n/oIy/LKcFudM7P/bWYrYq8vtQ04M3uFmX1T0jct8LZw2z5oZl+1MDvOzE40sx3hd37AzN5pZhPha58xs58Jp58dLvenwseXmdmt4fSS27Ytv698LizDfguOA89bYr28xszuDZf1DTO7LHx+nO2773vD138xtg39z67y9N03AAAoOoJnAAAM52xJayStl/RiSdea2VOHeP9PKwgeXCLphZJ+Mnz+/1OQmfM0ST8oaWvX+74TvveJkl4q6W1m9oNd5aqF5XqZpHeY2Wl9yjDSspxz10r6oKQ/ds6d7Jx7fjh/U9Lm8D2/L+kDZrYutrxnSrpD0lmS3iLJJP0vSXVJ3yvpXElv7FPWBWb2XEkflvQzzrmbzOwKSa+X9AJJayXNhq/LzE6R9E+SPhl+zgWS/jlc1G8oWL//NXxtv6R3dH3cj0m6UNIWSa+xY819j0j67wq2gR+RdJmkl0uSc+6/hPN8f7h+PqKgrvUeSRsknSepI+ntXZ91lYLf4UxJqyXNqLeRl2VmF0n6SwXBz3U69vsu5UclPTX8jr9nZt/bZ773KhY8C/eHp0n6UGyeyyX933D6C5J+08xebmbfZxYEkJexTUG22g9KukLSL4ef1XcbiNmqYBu8SMHv+V8kPUXBOnihpAfD+d4aPv80BdvLekm/F772GQUZclKw3dwRLid6/Jno62vpbXuQfeUbCravP5b0rl7rJ1zHvy7ph5xzpyg4jtwZvjzO9t33veE21FDwW9clnSHpnNgy++4bAAAUnnOOP/74448//irxp+Di8mFJB2J/hyR9LjaPk3RB7PHfSHpzOP0cSY9Lmoy9/lFJvxtO3yTpV2KvvaTHsn+0672vDad3S/rV2Gs/Hs5/Qp/vslPSq2Ll6sTnVRAg++EB18vAy4qvjyWWd6ukK2Lr4NvLzL9V0leWeN0paOp3l6SLY8//o6SXxR6vCH/PDZJ+vt8yJX1d0mWxx+skPSbpBEnnh5/3PbHX/1jSu/os69UKsqh6bj895n+apP2xxzdJ+p3Y45dL+uSAv9vAy1IQBPpw7LWTJB2W9OPh4zdK+kA4Ha2Dc2Lzf0nSlX3KcZKkg5KeFT5+i6SPd80zK2lzOL1S0isk/YukRyW1JL14md//uV3f65+X2wZi77009vqlkv5T0g9LWhF73iS1JU3FnvsRSd8Kpy+TtCec/qSkX5H0hfDxZyS9YMRt+1Yt3ldu71qvTtLZPd53gYL98sclrUpq+17mvb8n6brYa5PxbWi5fYM//vjjjz/+ivxH5hkAoGq2OudOjf40fGbEfudcO/b4LgVZGIO6PzZ9SNLJ4XRd0t2x1+LTMrPnmdkXLGiCeEBBJk+8ed+DzrnH+yx7kSSXFS7vl8zs1rC51gFJF3ctr/u7nGVm14VNzg4q6DerZ1PFmFdL+qhb3IfWBknXxD53n4IgyHoFGT/NPsvaIOmG2Pu+riBr5qw+ZV74jc3sKRY0l7w/LPsfLlV2MzvJgo7y7wrn/6ykU81sZWy2fttEkstatH055w7pWMZVPwOVK1zW9ZJ+KcySepEWN9k8VdL3SPrXcP4jzrl3OOeeLelUBcG2dy+R2Sb1+T209DZw3Hudc7sVZOu9Q9J3zOxaM3uigqy1kyTdElvWJ8PnJenzkp5iZmcpCFq+T9K5FjSLfYaC32LZbXuAfWVhnYfrVeqx3p1ztyvYJ94Yfo/rzCy+Tkbavpd5b/c21FZsGxp23wAAoEgIngEAsNghBRfRkbO7Xj/NzCZjj89TkDkjBZkrS713KfdpcROoc6MJMztR0t9K2iHprDDo9wkFQYKhJLAs17W8DZL+SkETsjPC5d3WtbxF71FwUe0kfZ9z7omSfmGAz98uaauZvSr23N0KsvVOjf1NOOf+NXztyX2Wdbek53W97wnOuXtj85wbm47/xg1J/yHpwrDsr1+m7L+loOnjM8P5o6Z+Q/92Yy5r0fZlQV9eZ4xQhn7eq6AJ5E8oGATg72Ov/aSk3c65I91vcs51nHPvUNA88KIllt/v91hqG1j4mK7P/HPn3NPDz3uKpN+WNKcg43JjbDk159zJ4XsOSbpF0qsk3eacO6wgGPibkprOublw8X237QH3lYE55z7knPtRBQEvJ+mPYutk1O17qffep8XHpZO0eBsadt8AAKAwCJ4BALDYrZKusqAD/+cq6Pun2++b2Woz26yg77DrY+99QZghdIGC/sIG9VFJrzKz9WGmzmtir62WdKKk70p63IJOxLcMsey4cZf1gBYHpSYVXLh/VwoGI1CQTbOUUxQ0n503s/UKghfLaSloOvcqM5sOn3unpNeZ2cbws2tmtj187R8krTOzV1vQEfwpZvbM2PveEgYzZGZrw76z4n43/B03KuhD7COxsh+U9LCZfY+k6a73da+fUxQEZQ5Y0PH6Gwb4rv2Ms6yPSXq+mT3Lgk7c36hkAxuzCppBX6ugad/h2Gvx/s4U/ibPMbMJMzvBzF6s4Lt9ZYnl/7YFAyacqyCAFf0eS20DxzGzHzKzZ5rZKgXB7kckHXXOHVUQ2HqbmZ0ZzrvezH4y9vbPKAh8Rf2b3dT1WFp62x5lX+n3PZ5qZpeGwfBHFGwXR8OXx9m+l3rvxyT9tAWDdqyW9CYtvpZYbt8AAKCwCJ4BALDYqyQ9X0Eg4EUK+gOLu19BlkxLQef5v+ac+4/wtbcp6APoAQWZOB8c4nP/StIuSXsUBBE+oaB/tSPOuYckvVJBgG2/gk7hbxzuawUSWNa7JF0UNuva6Zz7mqQ/UdCs7QFJ36egL6ul/L6Cjt/nFQRV/m7Asn9bQQDttWb2K865GxRk21wXNhO7TcGgC9H3/AkFv+X9kr6poJN0SbpGwXfeZWYPKejA/pla7DOSblcwyMAO59yu8PkZBevsIQW/2Ue63vdGSe8N188LJf2ZpAkFmU1fUNAUcFQjL8s5t1dBZ/DXKcggelhBn1mPjlGe+PKdgqaMG7S4yaYpyDyLl/WQgm3mfgXf5RUKBoG4Y4mP+LiCzK9bFWwz7wo/t+820McTFfxu+xU0V3xQ0v8OX3uNgt/8C+Gy/klBpl/kMwoCRJ/t81haYtsecV/p50QFAxzMKViPZyroF1Aab/vu+95wG3qFgoEg7lOwDu+JLXO5fQMAgMKyoK4DAADyJMwIe6dzboPvslSJmZ0v6VsKOmF/fJnZC8vMTlYQIL7QOfetFD/nGZLe7px7xhjLcArKeXtyJaumqmzfAAAkjcwzAAByIGzCdnnYjG29giZ5N/guF8rDzJ4fNtWbVNDn3VcVjECbtnGaqgIAAHhH8AwAgHwwBU2+9itotvl1Sb/ntUQomysUNDduSbpQ0pUu5SYIzrkvOef+Mc3PAAAASBvNNgEAAAAAAIA+yDwDAAAAAAAA+iB4BgAAAAAAAPRxgu8C+LJmzRp3/vnn+y4GAAAAAABAadxyyy1zzrm1vsuRpMoGz84//3zdfPPNvosBAAAAAABQGmZ2l+8yJI1mmwAAAAAAAEAfBM8AAAAAAACAPgieAQAAAAAAAH0QPAMAAAAAAAD6IHgGAAAAAAAA9EHwDAAAAAAAAOiD4BkAAAAAAADQB8EzAAAAAAAAoA+CZwAAAAAAAEAfBM8AAAAAAACAPgieAQAAAAAAAH2c4LsAAAAAAIBq2r59u+bn51Wr1XT99df7Lg4A9ETmGQAAAAAAANAHmWcAAAAAAC/INgNQBGSeAQAAAAAAAH0QPAMAAAAAAAD6IHgGAAAAAAAA9EGfZwAAAADQAyNBAgAkMs8AAAAAAACAvsg8AwAAAIAeyDYDAEhkngEAAAAAAAB9ETwDAAAAAAAA+qDZJgAAAAAAFcFAGMDwCJ4BBcPJDgAAAACA7BA8AwAAAACgIrgBDwyP4BlQMJzsAAAAAADIDsEzjKTRaGjXrl2SpC1btmh6etpziQAAAAAAAJLHaJsAAAAAAABAH+ac810GLzZt2uRuvvlm38UAAAAAkKJGoyFJtJQAgIyY2S3OuU2+y5Ekmm0CAAAAKK1ms+m7CACAgiN4BgCohCr01bh9+3bNz8+rVqsxuAgAAACQEIJnwDKmp6c1Pz+vzZs3l/JiGwAAAAAA9EfwDFjG/Py8Op2O72IAGNP09HTpA+BkmyFCFiIAAEByvI+2aWb/3cz2mtltZvZhM3uCmT3JzL5oZreb2UfMbHU474nh49vD18+PLed14fPfMLOf9PaFUDr1el1TU1O5vujevn27tmzZou3bt/suCgAAAAAApeI188zM1kt6paSLnHMdM/uopCslXS7pbc6568zsnZJeJqkR/t/vnLvAzK6U9EeSfs7MLgrft1FSXdI/mdlTnHNHPHwtAAAAr8g2AwAASE4emm2eIGnCzB6TdJKk+yRdKumq8PX3SnqjguDZFeG0JH1M0tvNzMLnr3POPSrpW2Z2u6RnSPp8Rt8B8IqLJAAAAAAA0uG12aZz7l5JOyR9W0HQbF7SLZIOOOceD2e7R9L6cHq9pLvD9z4ezn9G/Pke7wEG0mg0tG3bNm3btk2NRsN3cQAAAAAAQA74brZ5moKssSdJOiDpeknPTfHzrpZ0tSSdd955aX0MAAAAAKDiGLwFKA/fzTZ/XNK3nHPflSQz+ztJz5Z0qpmdEGaXnSPp3nD+eyWdK+keMztBUk3Sg7HnI/H3LHDOXSvpWknatGmTS+UbobCqMBIfAAAAAAAYju/g2bcl/bCZnSSpI+kySTdL+n+SflbSdZJeLOnj4fw3ho8/H76+2znnzOxGSR8ysz9VMGDAhZK+lOUXAQAAAOAPWT7IG7ZDoDy8Bs+cc180s49J+rKkxyV9RUFm2P+VdJ2ZvTl87l3hW94l6f3hgAD7FIywKefc3nCkzq+Fy3kFI20CWAoVbABxHBMAAADQj+/MMznn3iDpDV1P36FgtMzueR+RtL3Pct4i6S2JFxAYEhdgAAAA2aPedQz1UQBIlvfgGQD4QEUSQBzHBAAAAPRD8AyLNBoNzc7OqlarqdFo+C5OIXEBBgAAAJ+ojwJAsgie4TidTmfgecdNCY8CdIxyCQAAAAAA8ojgGRaZnp5Ws9nM7POy/KyqIYsQAOj3BwDygGMxgKIjeFYwS514fJyUOPkNxleFYZgsQgDVQ5AdcY1GQ7t27ZIkbdmyhaxwAACAEMEzoKSyziIEUExlD7L3umFB0BAAssUNdwBFR/CsYJY68XBSyi9+G0xPT2t+fl6bN28mmwO5UeUge16Dhj6zv6anpzk+AQAA9EDwDAAyMD8/n9nFOlk1wNKqHDQEAADA8Aie5US/PrHofwQoh3q9Lim9kWXjmW1SfrNqgCoYp59Lsr+QhiSzn+n4HQBQRQTPAKAE4pltZNUAAOKyzH4GAKCMCJ7lRL87d9yBLg6aysGntDPbAAyu1zmdbB34lOQ5gu23WOhzdXgcrwH0QvCsQmgCmj7u6qJsqED2FwXJOZYOh3MRAGSnV9YhN3wBYHgEz5BrSV64px0EoKkcUC3s79U0avCv6sFnAvGAH/2yDrnh2x/HKAC9EDyrEJqAYlRRyv/Bgwd1+PDh0l38VCkTZtgL2FF/Z5qJoB/ORQDgFzd8gfzhJlP+ETzDIo1GQ81mUxMTE5l/dq8DRpIHDg5Co6Oj4f5outcb20x6omOlmWnr1q1sexkj+DcazsEAgCohGFY+BM9yzMcO12w21W63vQTPkF9Ryv+OHTs8lyQdw14MNxoN7dy5U845rVy5Uhs3bkyxdMnK6ljCAAYAgCrJ64Vyq9VSp9NRo9FYOCf7vFkOoLc8HTfQG8Ez9BRd+GaJA0ZxVanZI+Cbz2PlIJ1M5/UCEuXE9gYsr91uL2qmWdWb5RwvkCW2sfIheJZjZdjh4hk6nKjS1b2uL730Uu4qpiSeqTYzM+O5NEC2aI4LAMfLax23Xq9rbm6u72vIJwJ9QP4QPANKKsu7ivQBhCTkNYOxVwU2avISTeelrGkbpJNpKvnIEtsbsFj3uRTHcLwAMA6CZ0gVQZX0dHdU372uo4yoMt9VZETH6snLndhms6l2p70wDQBAUbRarUX/kT8E+oD8IXgGFBQX7IzoWDZ5Dbb3rcCefWK2BQEAYBn9bqYCAMZD8AzAsnqN1AT4wJ3Y4eW1OSwAIH29ssyiftDK3DoBAJK2wncBABRD90hNeZHXcgEAUGaNRqPvqLsAAJQNmWcAlrXUSE15QJ8dQH95bQ4LoNiKeuMqL/2lZtWH51JZZtSfAGBwBM8AAGPpHrwiT/IywACQd3kJKABpo79UaWpqqrDBz3HRlQGAURE8A1B49NnhVxUr4K1WSzp4OJg+zJ17FB8BBZRVo9FYOE81Go2FOoPvoInPGzrT09OVPHcDwDgInpXMMHdTyMhAGUxOTmpqasp3MZBTHNuAweQloAAkrdls6lDn0YVpVBtdGQAYFcEzLNJrRB7kT/ddVCoBQLbq9brmVj8UTK8h8xEYBM2l4Evt7At8F8GbXnX6qB45MTHhoUQAUEwEzwoiyhIzM23durVvhXOYuylkZBRXs9nUI532wnTa8hpUrdVqvosAAIBXtCTAcnpl6U9MTFCPQk8cU4DeCJ5hkaVG5EG+1M8w30XwLuqovozGqbiMc0e5X2YInYkDGBfNpYDs9WqSzb4IAMMjeFYQRP3hE0HVYmk2m2q324k2x6AzcQDIJ+qIAJLEMQXojeAZUFJ5bWqZhCqkkyfxvUYJdva7G12UzsQbjYZmZ2fV6XR09tlnlzo7EQAAAEA2CJ4BJRM1u2u3276LUjm9gnrRcytXrtTGjRs9lzAZ8e956aWXeh28IgqORZ87Ozurubk5SdKdd96Z7offH4zepjXpfkyafHYaXYUgOAAAAMqB4BlQUitWrNDRo0cL39Sy1wW2jwttLvR7azabOpTh4BW9Pj+uVqvpwIEDOnr0qE4++eTUPndqamrhs7s7YS6SNJr4AgDyo9VqqdPpMDp7iSRdJ6WOCwyG4BlQMlGzu5mZGe3Zs8d3cSqlV4Ujem5mZibr4qQm/j1nZmZ08pmDv7ffgARJyaqZ5vT09ELwzPfFyLCV3vj8GzZskDRaE99xUUEHgPQxomZv0bnQzLR161bv53IA+UfwDMiRQS+CW62WHpp3kqSOK1+fZnF5ucDOSzmAvEk7IAoAGB19f5ZP0nXSPNRxyX5DERA8QyayvrjiAJysMg46AD/6DUiA0Q17jOvOHCyC7r7tAAAYB9cHAIZF8AzeRB1VR9NcFA1+Iq/X69pvD0qSTluXTXOrycnJQvftVCYEEpAnWQREffSnB5QJ/V4ByDOCmSgCgmfIRK+Lq2azqUcOpdPROAfgZEX9IVHhzgcCCQCAYbXbbc4fQAHRogbIB4Jn8GrqtBW+iwCUQjyrAABQXI1GQ7Ozs6rVaokd0+v1uubm5hJZFgAAVUTwDIA33ElLlo+sglarpUPz4fTj1eobj2bMANLS6XR8FwFATgxbR6Z+DaSD4Bl6ooN4oFjIKsgezZj9ou8/lNX09DTNKwGkjtGygeEQPMMiU1NTVNi60MlueopyN4yL9P7q9boePSEI2tXPzGbwCozGx53oND9znHNVNGDNxMREgiUCyo1sFqAY2D+BdBA88ySvFRDudvaWx052Ww86SdJp6zL4rIoHEPP22wMYT7PZVLvdTiV4RrAdAFAEWYyWnRd5vfZGsRA8GwM7YTXksTlcPEMwi36XarVa6p+RFPZLoDcf+0Pe98FoJOGkxJvASMUKoFXlJgnniNGxvgAAVUbwzBMqIBhHPEMwi4scRnAEgOXNzs6q3W4vTBctCJXHLGsAAMbFtTeSQPBsDOyEKIKqDf7AfgkAw8tjlnUaOEdkj2w/AINgAAPk3QrfBQCQjqmpKU1OTvouBirg4e8Ef0DVbd68WZOTk5qcnNTmzZt9FwcAAAAJIfMMKCkGfxhfdLd85cqV2rhx43GvRyP2RdNVvEOWdf97aWs0GpqdnVWtVqO5MoYWPwZU8XgA9EK2GYBBVGkAAxQTwTMAGFGz2VSn016YrqKs+9/LQqfT8V0EFFhZ9oNR0DwPAIqLYziwNIJnANBHVHGYmZnpO8/pa7MqzeCifu6K2t+dz8obGZtLi7ItJyYmfBcFAEZSlZFlAQDJIngG5FjUbIzKHYA8aDabarfb3oNnNJnOJzIVkkGQOn2MLAscj2M4sDSCZ0COUbHDKKJR8+r1uu+ijGSQyluUnSZJk5OTpQ2g5LUJhe9tq9lsqt05tDANFF18X9+wYUMugtRLKXIAuyojywIAkkXwDCioMnTODiSh3SGDoEoWAqdmsrNP910cIDW+g9RLCQLYjyxMY2l5vRECABgcwTMskkRTASoI2SjSXV4gaddff71mZmb0H3N7fBclVRxDgWPi9YtLL71Uu3btkiRt2bKl8OfE+L6+VD+beXLCWU/2XQRU3PT0tObn57V58+bCHwNQXY1Go1TnszIjeIbjTExMqFar+S5G6fkIMjYaDc3OzqpWqy30p4ZqKkKQm0oxeokCp1/97r2+iwIAA8nrebbo5ufnGSEbQGYInmGR6enpsS9SqSDkG5WMfCpCMKuftJoQUykGENd9bCSoDlRb1LSZYwGKLInrb2SD4BmQke6UXB8BkunpafomgaRkg9xpnfCrWikuciAVAAAAKCOCZwCQAwRJAABIz4H7vqkDrSNauXKl76IAyAFuVmJYBM+AhCw32EJRUnI5kQB+sd8BAAAA+eI9eGZmp0r6a0kXS3KSflnSNyR9RNL5ku6U9ELn3H4zM0nXSLpc0iFJL3HOfTlczosl/U642Dc7596b3bcAwmHb2+2xRipNUhIjpwJAHrVaLbmD88H0Y+a5NACK4NR1F+q8NaslSXv2lHuk5jzjJi3ygu0Pw/IePFMQDPukc+5nzWy1pJMkvV7SPzvn3mpmr5X0WkmvkfQ8SReGf8+U1JD0TDM7XdIbJG1SEIC7xcxudM7tz/7r5B8nrXRF/TTlwSgjp7JNJC8KZEbTRchA7NZqtdTpdLyWPxohtojrL69ardai/75xfkIS2I4AAEDSvAbPzKwm6b9IeokkOecOSzpsZldIek4423sl3aQgeHaFpPc555ykL5jZqWa2Lpz30865feFyPy3puZI+nNV3AZI2bsClKM1Eq6DZbKrTaS9MF1W73fZa/iKvOySrXq/rwVUumF6bnxsWQBl1D3hE3QLjIKANoKh8Z549SdJ3Jb3HzL5f0i2SXiXpLOfcfeE890s6K5xeL+nu2PvvCZ/r9/wiZna1pKsl6bzzzkvuWxQMJ61iaDabeqQEARcETl/ruwTjqdfrmpub812MXChTVkv0u+YlY7bo67PI8paFOI6ib0dl+i0A+FOm+gqQB76DZydI+kFJv+Gc+6KZXaOgieYC55wzM5fEhznnrpV0rSRt2rQpkWUCaVp/Bn35YLEyNAEFhsE2D/hV9Ez2Vqulhw4GNyNbhydzc7MAQHrImEUafAfP7pF0j3Pui+HjjykInj1gZuucc/eFzTK/E75+r6RzY+8/J3zuXh1r5hk9f1OK5QYKJX4CmZiYoOJYYM1mU4fISPSKu7fZajabancOLUwjHXnLQqyyXr8FF4KoOrKohsd6ApLlNXjmnLvfzO42s6c6574h6TJJXwv/XizpreH/j4dvuVHSr5vZdQoGDJgPA2yfkvSHZnZaON8WSa/L8rsASBaVpP5Oy2ET0Oj3MjNt3brVd3FQMnbW6b6LAOTKsOfIKjcFrdfrenz14WA6HG0TQD40Gg3Nzs6qVqstDAyVhKJnzCKffGeeSdJvSPpgONLmHZJeKmmFpI+a2csk3SXpheG8n5B0uaTbJR0K55Vzbp+Z/YGkfwvne1M0eACAxSeQmZkZz6UBAADD6L4Q3L17t8fSoCyKdKMy7+WLm56e1vz8vDZv3kwAZwCdTsd3EYCBeA+eOedulbSpx0uX9ZjXSXpFn+W8W9K7Ey0cAG+KVEnC8b8XQVqgP5rgYVzDniNplgtkZ35+noDQgKanp+mSAYXhPXhWNVSYkVdppU0DyL8iNuVyD4QJ5muPG1wbADCA5YKwXLeMJgpSs76AciF4BmABd8mQlFarpU6nw+iIOTc1NVXIO77xck9NTXkuzfDoiwUAgGMjak9MTPguCrAsgmcZo8KMvCJtutjinUFHdzx9ZxO12+1Cb1NVuONe1P0+Xu4y/i4AkAdctyANUV97krRixQodPXrUe/CsCnU+jI/gGbxptVpqHzwqSZosYJOhtLVaLT007yRJhxzrp4zS6qg3D9lEUf86aWq1WnrsYDh9mH0kz+g8GQCAckqiPkt/jCgCgmdjIkoNIA/inUEXNZtoKVFafzSdxbE2izvuUf+CZT93JNF5srt/n/bc96C2b9/OgCIAABRU/Bx+1VVXaW5uzntrCbIsMQiCZ/CmXq/rkaNBh89P4G7Dcer1ug7Yg5KkU9exfnxJM2hDAGBwzWZT7U57YVoK9pGDq4PstvqaYu4jZQty9kPnycDwfF9MAsAgqM+iKgiejamsUeq0mpMBvg2bLdpsNtXpCtrAjyec5bsE8MnOPl3ft3a9duzY4bsoi3C+RNLy0PQeyKPuOhyKL95yAsg7gmeoHC50MKwz1vguAQCgKsrY9D5P4gPsAMgH9sfRcW2bHYJn6IkdD2VV1mxRJKNqQ6Zn/X3LWMEry/cA8qKMxwkko7sONzMz47E0SAKZtvnAcXcwBM9QORwQAPTTbDbVbrcrEzyTpImJCdVqtSXniZrKjNvpP6igAr7RTAzIDzJtx0ddIjsEzzI0PT2t+fl5bd68mcwXAMixqlxUZZ2JmWQFb2pqauT3lqXZFoG40bHu8ovfY3hszyiqqmX85xXHjcEQPMvQ/Pw8d+0BAJkYdnCMpURBtpmZGe3Zs2fo97daLXU6nURHrC3qTagyVlC5cAeA8kuyXhE3SAY8kAcEzzIUZTIUtcIPIH1chI6OdZdv7XY7N00zytJsi+18dKw7lAnbM4qKvohRJATPVI0Lrip8xzK690EnSTp1neeCoKdWq6UD89KRI9KD3/mqpqen1Wg0fBerNOLZShheniqkUbAK+TVOE1bqFQBQflG9Yvv27brhhhu0c+dObd26NTd1DSBtBM+AnIqPPjNO3z7IhnNO8/PzYy+Hi9DFhslWYt2BG0XjmZyc5HyDgbRaLT1+sB1MPzbpuTQAAN+qUAcjeKZqXHBV4TuOIs87eXz0mTzd0Umrv4Miqtfr0sogm6bz8GThm4DlzTjZSmyn6ShLR/s4Hl1LAAAGkbdrJiArBM+AnGu1Wtq2bZskggCorlarpUcPhtOPlSNwE40wFU3H9+08Bf/iI0XnHRV6IBv1el0HVgWDYNXXMkoeACQlz8kdSylSWUdF8Ay5lNWFYxV28qTlqR8loJ8ibKfNZlPtTnthOq/iI0WXpaN9IM+iwPrEBEEpDKdIF91ZlrVI6wVAfhE8Q2VFnZDn/QK7Xq9rx44dvosBeFWv1/XwqqAJZ31tiQI3Z/fuK6gIwb9h0NxzeFzsVdvExIRqtdpI72XbyU48MzfPx+xGo6GdO3fKOcd2AeQc+2d+ETxDLmVx4ZjnTA8AyJNhBm4AMJ6yBc/LLJ6ZmwdFuujOsqxJfhbBaaC6CJ4BSA0VDKD4xhm4oXsZNPccHMfMahj3PNkri55tJztFGWijrAHZVqulTqdzXL+hw6CuCmBQBM8SwoG3PMr8W9KPCoBhxZtcEvzCoKJzqZlp69atpbxwzwMyQsslT4PFFEXWmdFluzYAMDiCZ4AWB8zKrNlsqt1uZxY8o4IBAEB/nCeB0SWRGe1zHyzzDXugjCodPEvy7g4HvGKJMrCi6bgq/Jb79+/Xli1bOFkXUKvV0sH5cPpI787X85ZhmGbl8PD94cSaRBeLGJpcYhScW4DhlbV5pQ8EpgAkrdLBs15Il66GZrOpRzrthem8nlSnpqZ8FwEDePgh6fAjnVyNJDjOSG295HG0xKmpqYUgOPtKebVaLbkwYtx6zHrOk/ZFUhkvwhqNhmZnZ1Wr1Y67iQQAgyrj8TErrC+gWCodPOPuztLKHkjccHrvi7A8SWudb9y4UTt27Ehl2VX0+GPS0aNHM/mser2uoyuDJgr1s3pnAuXt2JZW5XB6enoheJan74vj5SnoimOyGCWQC2sAPnC8AZC0SgfPesnbRSf885Fxw8VGMZW5WRtN9zCuycnJkTIE6/W6Hlzlgum1vbe/UY+Te/fuHagJexmPw/HgMwCMqozHx7Ip+nVFr/IX/TuhmAieLaPKO2aZA4mtVksPHwguxk4WGRFlFjVHKuu2DBRBFHRlP6yeqtWd8iqv2Z/T09Oan5/X5s2blz0+NBoN7dy5U865StbLAQB+VTZ49s1vfjPzDtNbrZY6nY4ajQYXEAXiI+OGCmFyyKxAt+6bIvHHGzZsyKwcrVZLOhg0m2sdzueFbdnRhB1VMmz2Zxbdd8zPz2fSfHhQVb5pjvLKYltO83jRq/zsn/ChssGzQSW9Y7bbbS7mc6Ber+thPShJOplmaEAhPPJAOLHWazEAYCw+AjR5zf4cplx5bBHBjXEAqI7KBs8uvPDCheh4VqIMJqBKuu9E7d69m7u6Ayr7oB3DSHJkze7tLv54ZmZmrGUPo16va251kHFRX0MQH0C+5DFYJWWf4bIcbowD+T1e5BVZrsVU2eAZcNe+oM+zjVyzSgoqo81mUxMTE76LkpjoO0XTnNSLi5E1UQVUpquB37Y8uDGOUXCsB4qJ4BkqKckslrJoNptqt9uJB8+670RlGfhoNpvqdNoL00WT9l08MtuAYsnTPsvF3+BYV8kiwwUolugYaGbaunUr+6+4iVJUBM9QSWSx9JflwAhZWLPGdwmykdeR1JCMol98D9svUJaDOOQpIOXzt6XvJgDIRhHP4wAIngGFUfSL5yRw52ppw46kxt378kgiANRoNLRz50455xI/ztRqtcSWVWVp7rPD/kZVPQ+Noojrqmx1jvn7bw8m1lzEzaYBpHk+QPWw/aAsCJ4BKK1Wq6X5+WD66NH0KstHjhz7PF/6jViWp6wajK5XxTN+cXvppZem9tlJbNeNRmOo+bMcxIEgcmDY36gKonXC9lFs3V11tFqtoW82DSurcy/neJQt0A3kWWLBMzN7laT3SHpI0l9L+gFJr3XOZTukJZCx6KSVNk6IrINjmXfSaWf6Lk05RYGiomUmJBEAWmoZ0YVmEfsOBEYRD0pI1Quglel8291VB912LI+bCgBwvCQzz37ZOXeNmf2kpNMk/aKk90sieFYRRbv7NcodR+7uFEu9XteKFcEoWGefPVpfbvHsNdcne23lSunxo/nsL44KcD4tBN1N0rrJkZaR1TEontWYdhYYkBfNZlPtziML01ga9aPFsjr3Dvs5RaurY3nsb0B2kgyeWfj/cknvd87tNTNb6g1Ac/9RSdLGc7L/7KQqDNFJa2ZmRnv27ElkmWVH5W00119/vWZmZnTPA+lsZ1z8BIGiubm5XAZCk8Q+CBwvfgxctWqVdEJQTS5aJiqSxzFzedQhAJRdksGzW8xsl6QnSXqdmZ0i6WiCy0cOLFV5GPbuV3cfFHkTVQJWrly58ByVgaU1Gg3Nzs6qVqsN1X9OmhWuuSDxTGefPdr76/W6LMxeWzdi9loRdQ/OkOQyqVgfC4TumSOjBewbKL6qbrdFa+pPNjoAjC7J4NnLJD1N0h3OuUNmdoaklya4fJRM2fqdKFoFKi2dTmfZeborb7t3706lLHkP0OZN/OJn+/btHksSKMs+tWRg5P528H9NtmXiAgo4XvdAFXP79krKZ5N8ZItj5vKqGkAFUB1JBs8+7Zy7LHrgnHvQzD4q6bIl3oOCyVPlIe079TTHHF48IDqMtCpcZQvQxu3/jrTvgT3avn17qtt/JIm+rqpWsV5uMBGCu4hUbd8oAvZP9NJd96xKU/9eyJgFUDVjB8/M7AmSTpK0xsxO07G+z54oaf24ywfyqFeFocoVKBRbXivA3ftUvwvYvXv3asuWLbkrf6Rfucoc3M2DvG7XRTdq83xfRu2rqrtbCgAYRKPRWDi3NxoNjh8oBfp9DCSRefarkl4tqS7pFh0Lnh2U9PYElo8C8HGRwsVQuqKLoqoeHPPutDOlc866RDt27PBdlMwUbVvkGIWyGqR5fhnk/ZjDRXr2OK4fw7rordls6pFDjy5MAyiPsYNnzrlrJF1jZr/hnPuLBMoE5F4VKgxlOeHT3GZ5Rd6ep6amNDU1xUVjwSV5RzO+rG3btrFtJCyeMVmEO9F56m5iEMPcuGo2m2p3HlmYztrjD9wRTKzdmPlnA1kb5nj35NMvyKpYQCaKdi5NS2J9njnn/sLMniXp/PhynXPvS+ozkF9FvvhGuXGgLzd+Xz/y3lS2SooQwMLghg2CrTzrvJRKsjT6hAOQF5wHkZXEgmdm9n5JU5JulXQkfNpJIngGAEACytqcOsk7mtwdzQ7rejhF6Idv0DJGGYh79+7VDTfcoN27d+f2OwFJ4HiHYRS5vkYwsr8kR9vcJOki55xLcJml0mq1Fv0HUHz7visdPeq7FKiKvDSn3rhxYyn62yvD+ZgLOgBAEaR1AyGP58G81NeQrCSDZ7dJOlvSfQkuExhKEe7qEs0vj6jZSqfT0dElImitVksH5sMHR4p/sT6M2267Tdu2bWNbL5miB53iTc66ZXke4XxQLXmtl8QNW8ayBNIBoJciXFsmLY/ByLxIMni2RtLXzOxLkh6NnnTO/bcEP6PQ6vW65ubmVK/XfRelkHxdZBT9IjFL0chfExMTvouSiajZSrPZVLvd9l0cIBWtVkudTkeNRmPJoFMRRJVgM9MZZ5zB+TjnqhZcZPRMdKvihTvKi20YRZdk8OyNCS4LQ+DEekxa339ycjKxDnG7o/lF//3i5d+wYYPa7XZlgmeDqtfr0sq5YPqs8S/W9383+H/OWWMvaiyDbLsXX3wxWQkFV6vVFqbjIy2WVZbH4are3e117Gg0GpqdnVWtVlvoK6ZqBhk9M76eJicnsywegDEUvb6fF1mvR34rxCU52uZnkloWqmXQUdt8XWREmQlVvMAZFdkc6WGEMwwiycplmQIZ8XUxMzPjsSTotmfPHu3bt08HDhxYyLqqYnBxxVnnLjtPp9ORpNIEz1qtlrZt2yapOBmG0TF25cqVqX4OF+4AkB9Jjrb5kILRNSVptaRVktrOuScm9RnojRNrsRX99+NiNFvxzB/fFxhpb7t5azLNXePqqFpzwaz12n/m5+d19OhRHT16VLOzs97WeaPR0M6dO+Wcy+W+Xqbsz6iZ6qOPBr29nHjiiZ5LVAyci4qJ3yoZrEf4lGTm2SnRtJmZpCsk/XBSy0d50dksgH6SbDKdR2l9t7JVLt0D+4KJtev9FgTpWr3adwm8arVaOnrwoWD6sYc9lyZ98Waql1xcrLpgdIydmZnRnj17PJcGAJCFJPs8W+Ccc5J2mtkbJL02jc8oM+4oAcPLw36Tt0ypostbk+k0tqthvltVOxP30VS5Cs0F8zbAS71e19y+fQvTvlTht8+TJ5x9ge8iFA7XBkC+VbW+VgVJNtt8QezhCkmbJD2S1PKRDpqmVEsU3IkHeaJtIOpDBcMb5OJzX9jJf91zJ/8oriBL49DCdFXkqalymUSjBOcleNZut7VC0ooVKzILkuatDlSv17Vv1cFgei29ngDL6VWvBZIwzk35ZrOpRw8tPfhLmeTtXJqmJDPPnh+bflzSnQqabmJI3FEChudzv1kuS2LczBmy6rDg7JN9l6BSon3PzLR169ahK4R52HeXM2yWV1oZa5dccsnCuipLxTtPFxStVkudTocsCADIwAWnM3haGSXZ59lLk1oWskPzhPKLX7xt2LBBc3Nziy6Wom0g3m9HldKNs7i4LUvmTNn7HwOwvLQy1nzUR6pUB6rVar6LkDvRSMJV2QaWU4Rgf7d6vX5cvbaqivj75RnrcHBVOpcm2WzzHEl/IenZ4VOzkl7lnLsnqc8omu47jkBRNJtNdTrthelB5T19vqgVizyUNW/9jyF9Rd1fkrTU946vn0svvbRnhlGZ1xsXq8sb5YLi6AN3BxNrNyZalihQhGOq0JwK6Ma5PV3R+l1pK3Th6QxyVDZJNtt8j6QPSdoePv6F8LmfWO6NZrZS0s2S7nXO/bSZPUnSdZLOkHSLpF90zh02sxMlvU/S0yU9KOnnnHN3hst4naSXSToi6ZXOuU8l+N1yhwMfBhXfPmZmZgZ+37oz0ihN/iS9/+SpmY5PeQ+k5kmj0dDs7KxqtRoXuBgZ9YLiS3twDM5PWArHjWLj9xtdUc+fRS13kSUZPFvrnHtP7PHfmNmrB3zvqyR9XVLUO+ofSXqbc+46M3ungqBYI/y/3zl3gZldGc73c2Z2kaQrJW2UVJf0T2b2FOfckbG/VQ+DbqjddxyHCVwARZT39HlOLMirPA7Ywf6ytO71QyAC40qyiT+Bsv6i/t8mJiYyr69MT09rfn5emzdv5jfBstLYjzm3p+v666/XzMyMDt+733dRkIIkg2cPmtkvSPpw+PjnFWSHLSls7vlTkt4i6TfNzCRdKumqcJb3SnqjguDZFeG0JH1M0tvD+a+QdJ1z7lFJ3zKz2yU9Q9Lnx/9a+cSBD8inKrX7X0reA6nL2bt3r7Zs2ZLJ3bz4BTMwKuoF1RAfsGHY4yvnp4DP/t/m5+dzebMEqLKinj+LWu4iSzJ49ssK+jx7myQn6V8lvWSA9/2ZpP8h6ZTw8RmSDjjnHg8f3yMpajC8XtLdkuSce9zM5sP510v6QmyZ8fcsMLOrJV0tSeedd95g36oHNlQMqkjptPFmdkUNeOQZI50BAMY16IANBMr6i5rHJ9EiZNiuCeg/FMNgPwbyJcng2Zskvdg5t1+SzOx0STsUBNV6MrOflvQd59wtZvacBMvSk3PuWknXStKmTZtc2p+HfMg6gEUfT+Mpa1MTRjorlo0bN2rHjh2+i7FIq9WSDh4Kpg9znAGykHUdYtC+zrjJlR9FH4k6yXpXWetwwDBarZba8w9JkiaNTNMySTJ4dkkUOJMk59w+M/uBZd7zbEn/zcwul/QEBX2eXSPpVDM7Icw+O0fSveH890o6V9I9ZnaCpJqCpqHR85H4e4BMxDv6jeQ92yyu6M3s8i7tjuCLltkWVbDb7WBU114Xpj6/E0FwYLGFEcRWrvRdlFIrwvEbx5BJBgDVkWTwbIWZndaVebbk8p1zr5P0unD+50iacc69yMyul/SzCkbcfLGkj4dvuTF8/Pnw9d3OOWdmN0r6kJn9qYIBAy6U9KUEvxsKLKsAFv0WJYMU9dEUPbNtfn7+uD7GfHynXkHwvKjX65pb/WgwvYYgN5CFIt0EA0aRZL2LOhwQ1NcOhzlFq+uneS4NkpRk8OxPJH0+DHxJ0nYFgwCM4jWSrjOzN0v6iqR3hc+/S9L7wwEB9ikYYVPOub1m9lFJX5P0uKRXpDXS5jjIZACQluUy2/LW/153BTsqX1za2Xq9EAQHeouOGzMzM9qzZ4/n0viRtyZprVZLRw4+HEw/9pDXsgBpyVv9BcXC9oMkJRY8c869z8xuVjBSpiS9wDn3tSHef5Okm8LpOxSMltk9zyMKgnK93v8WjR6sy0zR+0UYFwewZOV1fRIoxrDytP2iOPJ6DER68hbAgj/s/wCALCWZeaYwWDZwwKwq4v2EbNy4kYoeSivPTd6qjgsLABhP3pqk1et17V8VZJzV156yzNwoqqoHjKm/YBxsP0hSosEzYDlZHsCqUNnI2wmBJm/IKzIUyonfcnjRubHTKeYIYL4CWMMeQ5abvwp1lCT1Wp/j7P+NRmOhvlKUgXYAAH4RPEtYd7898ZP8zMyMr2IBGMODc8H/dWf7LQcA+BY1y6d5Poqs2WzqUOfRhekkJX2zJm8Zj0BWGo2GZmdnVavVvPSDC3QjeIbSorKBJMSbola5v8KiI0MJCETnxip3/D+KYY8hy80/ah0lHrys14s76u709LTuuusuuRNP0aramcvOn8Yx/NSzL0h8mcBSfGacFjXbtahZ0rfvC47VF61ntM0yIXiWMC7QUAatVksHwwTKR121swviTVGLUtFAid0fjKynNX6Lgeqq1+uam5srdOAG/s3Pz+vo0aMy3wVJAdcCQDKK2h0MN97Li+AZsIxWq6VOp0OfGAC8ojIGoCzBy3q9rk6noyMDZJ2No3vQLsCnpTJO084Mo0VOdrjxXl4EzyDJXyrvoBeAPjv7rtVqmX5eHtTrdZ1oQUdfZ6wrdgU9C1GAdWJiwndRUGJUxgCURXTeXJ1RFWvlypXcdEAhtNtt3XDDDdq9ezdZjEhEUZvs5hHBM3hVhJ2XDioxiImJiUoGWoEII5oW0969e7VlyxZ+Nwxt3GDU0aNHEypJf2zTKIooM6x78Lkqi0bF5eY08oLgGSQtncqbhwsiKj/Is3q9rh07dix6Lg/7DQAAaRnnBmjU/PTRuW9LklqHJ5MqVq7RFUix+KjLUWc8ptlsqt1uEzwbE012k0PwDEBiuEMEVBcV/mLauHHjccF/lAc3cvKn3W4XshN0wJei9/GI8iB4hmVR2cIwaL4YyGq/4cIIQBzHBBRBqxWM5L1i1RO0qnam6mtO9FyibEQZdygGjqEA4gieYWBUyLEc0oKzQafHAIBBUF/DsKjvIy+iIHv0H/CN4BkAFEw8QEnFFkAcxwQUQZSBtap2pu+iAAAwEIJnGBgVcgAoJzIN4APbHXxptVp66GA7mK7IYAWDYl9EXkRB9rz1eTbIuYtWIuVE8AwAugxzQcfJEVnyvb0xKAiwtKwCgq1WK3cXlMOgGRaAMqMbm3IieAYMoNFoaNeuXZKkLVu2cEDEArYFZCmt7W2Yi3wfg4L4DhoiHUttd2Sl9TY1NZX4SI2+1vWKFSsy+6xu9XpdR1YfDqbXrPZWDgDZaTQa2rlzp5xzYx3vqnxOqvo1McEzAOhS5ZMisBRfg4Ik/Zlk0I2PzKHe0j5/TE9PJx4886Fer6vT6eiI74KMqdVqqdPpqNFoVOYisuoXz8helucbbtxgKQTPMlTFE2xZMIokgLREgZxommNNNnxk0OXJqKOYpZH51AsXLdnxsa6jOrHpO4UeNKDKxxAgbUmfb7ieG1/V1yHBswxxgi23smUy3Pdg8P+MdX7LMYruu6KSNDs7q1qtpkaj4bNowHGazabanfbCNNJX9crfOMqS+QS/arWaDhw4IOe7IGOqYp2C4+fSWq2W2vPBOX3SGIxiHD7ON9y4wVIInmWoiifYqilLJkP8Tk9Z+hrqdDq+iwD0dzYV7LLKaxOnvI5ihmpoNBqamZnRf8496rsoXtx2223atm1bro4Jg6BJG4AqI3gGJKRMd+Lid3qK+J16/RZkSiBN0QWFJE1OThbugggAAIyvXq+r44LBKCbqDEYxjrK16smTvN7YyzuCZwCAZdFnIzCaMt1YAZCMiy++WDt27BjqPXnI+spbthkDl5RfWVr1oBwIngEAlkXFZWl5u6AAkJ48BDEiRx74djCxdqPXcgC+TE5OlqaLESzGzaf0sG5HQ/AMALAs+mzMwH1t7Wnt0fbt271fkAPIvzL2T+rLOAHRYZo/jTrKrcRNml6iPhsJAgC9LXdso/nmcAieAQAQon8NAMvJSxCj6P2TAgBQJATP+vCRkk/kFwD889a/xrpJXbJmauh+cABUBwH+5By4/3ZJ0rlrLhqrrj9M8ydGuQWQpeWObTTfHA7BMwCL0PkqqoxKBIC8owPt8dHkFSi+RqOhnTt3yjmXiz4oUX4Ez/rwsfNV6aItT53tIhCvSJZNknfq2XYBAL5Uqa6YJpq8AgCGRfAMgKTFFcmyaTabarfbNHMBAAAASoCbCcgawTN4QcYOfEiijxG2XaB46FMUAAAA4yB4BgAlQYAAQNrosB5ZoqsEZCWJbS1axgpbqanTL0y4hKgS6vT5RPAMqCAGBUBaoorjypUrfRcFWEDTjmTRYT0AAKgagmdAhZR5UAAQIACQPo4zyBLZZshKEtva9ddfr5mZGXXuPZxAiVBlnGvzieAZUCFlHhQA+RBVPmdmZrRnzx7PpQEA9JOHJpGP3H97MLFmo5fPBwBgUATPUHh5qPyV0dTUlO8iAACAkopnw1PnQBHRLxVQLQTPAPREBeCYNCv1VLwAAD74vuEYz4bn3AcAyDuCZ56RNTU+1hvSRqUeAJB31CmRF1XZFumXCqgWgmcASi8aXTSPo4xS8fKnKpV7AAAA+FPWliZVq0sTPPOsChsZAAAA0kWdEnmRl22xrAELAH4QPANQevV6XXNzc6rX676LghzJS+UeQPq4iM6/rDMYfAxSkMcMeADpK2tLk6rVpQmeAQAAAKgUXxeyk5OTjC6akbIGLJAtbr4gQvAMAAAApcZFdP5VIYMhyoDv3ha5OAeA/CN4BgAAAAAA0KXXzRcC3tVE8AwAAI9arZZ0sBNMH6Y/HACoGjIjASD/CJ4BAAAAAAAMgIB3NRE8AwDAo3q9rrnVQeZZfQ0jwiI98dEMN2zY4Ls4WEbWo09moYzfaSnR9zUzbd261XdxAABjIHgGoDIGGSK+0WhI8jcKFwAAg2LURgAAskHwbEBVu1OG8RShE8lGo6GdO3fKOVf67XpqakrNZnOgeQedD9mo0nZaJkU4BlZRfP+ZmZnxWBIMYpDjXdH2rSIdw5Oo+3e/r2r73bDrsIrXW2Wr51TxN0R1EDwrOQ5gyAuf2+L09DRBMQDoYZCMXAAAgKojeDYgAk/5lrcshyJ0IlmEMqK4krogZzstJn63dCVxM2KYjFygiqj7j2/YdVjFdV6282UVf0NUB8GzkuMAhrxgW6yeyclJ+uMBcoqMXAAAgMERPEMplO2uDVB09XowaiT7JZC8Mt2MyFvmOJA1ulgZT6vV0rZt2yRxDMkbju8omxW+CwAAedFoNNRsNtVsNhdG3QQAAACAMti+fbu2bNmi7du3+y5K4ZB5BgChZrOpTqe9MA0ASFeameNk9KAI2DbHU6/XtWPHDt/FQA+0DPKH8186CJ4BQMwZa3yXAAAAlFGr1VKn01Gj0SCokEN5b2ZIQARJYNsZHcEzAKUXNcecmJjwXRQAQEbSvkDgQhbDqtVqvosAoAI4J6WD4BmASpiYmKDSCgAAvKE/1WQlncmX92aGPgMi3CwACJ4BCJU5O2vQylCr1dL8fDDtjrZSLhUAoMi4gBwfzRhHk/fmhVnhpijiCPAhbQTPACwgOwsAAGSFOgfGEc/kiwInZqatW7dWNqCYFoJRfrBd54vX4JmZnSvpfZLOkuQkXeucu8bMTpf0EUnnS7pT0gudc/vNzCRdI+lySYckvcQ59+VwWS+W9Dvhot/snHtvlt8FKLq8p6pnoV6vy1bMSZLWnV33XBoAAMqNZoyjoc7Wn3NON9xwg3bv3k3AZwxFzG7k90bafGeePS7pt5xzXzazUyTdYmaflvQSSf/snHurmb1W0mslvUbS8yRdGP49U1JD0jPDYNsbJG1SEIS7xcxudM7tz/wbAcAySCsHMIxGo6GdO3fKOcdxAwB6iI6LUR2r7IoY3MLwON/ni9fgmXPuPkn3hdMPmdnXJa2XdIWk54SzvVfSTQqCZ1dIep9zzkn6gpmdambrwnk/7ZzbJ0lhAO65kj6c2ZcBAAAAco5mQCgzgg3JILsROJ7vzLMFZna+pB+Q9EVJZ4WBNUm6X0GzTikIrN0de9s94XP9nu/+jKslXS1J5513XoKlR5bI2kFcEe+8sd0CGAYXMemiXoG8YZsstjv23S5J2rj+otQ+g/MCkL1cBM/M7GRJfyvp1c65g0HXZgHnnDMzl8TnOOeulXStJG3atCmRZQIolweDLs+07my/5QCAcRXx5kIRFS3QUYQyAkU1NTWlZrO5MI3yKNqxHsnzHjwzs1UKAmcfdM79Xfj0A2a2zjl3X9gs8zvh8/dKOjf29nPC5+7VsWae0fM3pVlupGe5AxMHK8QleeeNCg8AFNeowULqFcgbtsnimp6eXqhLcsMCZVXVQKLv0TZN0rskfd0596exl26U9GJJbw3/fzz2/K+b2XUKBgyYDwNsn5L0h2Z2WjjfFkmvy+I7ACgPKjwAyoRmPdmo0oXDqMiCBFB0HOvhO/Ps2ZJ+UdJXzezW8LnXKwiafdTMXibpLkkvDF/7hKTLJd0u6ZCkl0qSc26fmf2BpH8L53tTNHgAiocDEwAAGBbBQiB/CJyiCqqWiVWF79iL79E2PyfJ+rx8WY/5naRX9FnWuyW9O7nSAQAAHFO1yrEPrOPiWipIQmATAFB0vjPPAKAyuPsKAEDyOL/mVxqBU4Ls+cDvcEza3z+rdc1vujSCZwAA+HZ/O/i/xm8xsDQqkuljHRcX2WUAgDIjeAaMiLuc5ZTmKJtcWKAXRnkFgPFwfq0Wguz5wO+QnazWdfxzyEI7HsGzGDYQIJ+yDFRS+UbWGOUVAAAAyDeCZ8CIuMsJAEgbN/ZQNNENr3Y7aI6e522X/QsAeuOYeDyCZzFsIEA+EagEAFQVAR4AAPwjeAYAJcUFF1B87LsomiLd8GL/AoBkRdcfZUTwDKnhwj1/Go2Gms2mJiYmfBcFAJCRcc7HDI7jH3UoAAD8I3gGVMzExIRqtZrvYiADXHDlBwEIAACKh/M3MJzo+sPMPJckeQTPkBou3POnSE0pAIAM5mSMs+44b8AHAhbA8NhvqoHf2R+CZwAApKysAYjp6WnNz89r8+bNpfx+AIBqG+T8zY0e5EWj0dDs7KxqtZoajUYiy2T7PobgGQAAWDDMHc35+Xl1Op3UylL1Slqa6AMTeVbWGw5AmthvqmG53znNelnVETwDAAAjqdfrkkRlvaDK1Aem7zvjNKMpD35LDKvMN3p8H1vLLun1Oz09rWazmUDJjuF3P4bgGYDc4ASNMij6dsyd62rgdwYAABgcwTMAADC0qNlfNE0gBj75DlQTjCwPfkvgGDJ50+X73IXhEDwbQpV2ZMAHTiAog6psx81mU+3OoYVpAAAAoKwIngFIXNGbrQEYjJ11qu8iAABKhGQFkP05OloFpIvg2RDYkQEAAID86HXDjpt4yWJ9AsXQbDb16KHOwjSSRfAMQOKoWAEAAGBYJCsA47ng9LN9F6G0CJ4B6Is7jcDSqryPtFotuYMPBdOPtTyXBkBV9Tr2Vu14nDbWJwBIK3wXAAAAAAAAAMgrMs8A9MWdRmBpVd5H6vW6Hlx1JJheW/dcGiSpyhmVAAAAvRA8AzASLq4AoNzm5+e1ZcsWjvMAAK8YhXUwrVZL7fmDkqRJO+y5NOVDs00AADAS98ABuQcO+C4GEnb99ddr165dqtVqvosCAACQC2SeFRgRePhEFkL1cMxB3NTU1MIw6FNTU55LgzRwnK8Oju8A8myYUVir3DqmXq/rsFstSVpdX7PotSqvl6QQPAMAAEObnp5eCJ5xoQ0AAIAyI3hWYMNE4AFgXBxzAKCcOL4DKAuyqnpjvYyPPs8AAPCo0Wio2Wyq1Wr5LsrQWq2Wms2mGo2G76IgJxqNhrZt26Zt27axXQAAELN9+3Zt2bJF27dv910UjIDMMwAAMtKvv4mJiYlCds6eRJnpgwPLYRsByom+9oDk3b7vfknSRevXLDMnhkXwDAAAj4rcXIrMInQr8vYMAElptVratm2bJAKDOCbtG0AM5pQugmclFd2lNTNt3bqVAzYA5ABZM8djnWA5bCNAORFsB5LFYE7pIngGAAAAAEBC6vW6duzY4bsYABJE8KykuEsLAAAAAAAwPkbbBAAAAAAAAPog8wwAAAAAkBuMsgsMr9FoqNlsamJiwndRSongGQAAAAAAwBDyGOSdmJhQrVbzXYxSIngGAKi8RqOhXbt2SWJIeQAAfMtLIAIoEkawTRfBMwAAAAAAgCEQ5K0Wc875LoMXmzZtcjfffLPvYgBAKV111VXqdDpkcQEAgEqhDgRIZnaLc26T73IkicwzAEDi6GsBAABUEXUgoJzIPAMAAAAAYEB57Cge5Vek7Y7MMwAAAAAAACyrSAEvLI3gGQAAAAAAAyIIAh/Y7vwieAYAAAAAAJAwAl7lQfAMAAAAAAAkgqaKKKMVvgsAAAAAAAAA5BWZZwAAAAAAIBFkm6GMCJ4BOdBoNLRr1y5J0pYtWzQ9Pe25RAAAAABQLlx3YVQ02wQAAAAAAAD6MOec7zJ4sWnTJnfzzTf7LgYAAAAAAEBpmNktzrlNvsuRJDLPAAAAAAAAgD4IngEAAAAAAAB9EDwDAAAAAAAA+iB4BgAAAAAAAPRB8AwAAAAAAADog+AZAAAAAAAA0AfBMwAAAAAAAKAPgmcAAAAAAABAHwTPAAAAAAAAgD5KFTwzs+ea2TfM7HYze63v8gAAAAAAAKDYShM8M7OVkt4h6XmSLpL082Z2kd9SAQAAAAAAoMhO8F2ABD1D0u3OuTskycyuk3SFpK95LRUAAAAAAEAKGo2Gdu3aJUnasmWLpqenPZeonEqTeSZpvaS7Y4/vCZ8DAAAAAAAARlKmzLNlmdnVkq6WpPPOO89zaQAAAAAAAEY3PT1NtlkGypR5dq+kc2OPzwmfW+Ccu9Y5t8k5t2nt2rWZFg4AAAAAAADFU6bg2b9JutDMnmRmqyVdKelGz2UCAAAAAABAgZWm2aZz7nEz+3VJn5K0UtK7nXN7PRcLAAAAAAAABVaa4JkkOec+IekTvssBAAAAAACAcihTs00AAAAAAAAgUQTPAAAAAAAAgD4IngEAAAAAAAB9EDwDAAAAAAAA+iB4BgAAAAAAAPRB8AwAAAAAAADog+AZAAAAAAAA0AfBMwAAAAAAAKAPgmcAAAAAAABAH+ac810GL8zsu5LakuYkrYn914DPJTm/z8+u2vxFKmvR5y9SWYs+f5HKWvT5i1TWqs1fpLIWff4ilbXo8xeprEWfv0hlLfr8RSpr0ecvUlmrNn+RyjrK/JPOubUqE+dcZf8k3dz9f9Dnkpzf52dXbf4ilbXo8xeprEWfv0hlLfr8RSpr1eYvUlmLPn+Rylr0+YtU1qLPX6SyFn3+IpW16PMXqaxVm79IZR11/rL90WwTAAAAAAAA6IPgGQAAAAAAANDHCb4L4Nm1ff4P+lyS8/v87KrNX6SyFn3+IpW16PMXqaxFn79IZa3a/EUqa9HnL1JZiz5/kcpa9PmLVNaiz1+kshZ9/iKVtWrzF6mso8xfKpUdMAAAAAAAAABYDs02AQAAAAAAgD4GarZpZs+VdI2klZL+2jn31q7Xny/pg5JOkuQk3Svpnc65t4bv/UtJTwpfM0lHFQTujoTL7HY0nM+WKJZb5nUAAAAAAAAU0+MKYj+HJa0On/uOpH+U9EOSnhw+f6KkQ5L+TdIvOOfukSQz+yNJPxW+7w+ccx8JnzdJb5a0XUFcquGc+/OlCrJs5pmZrZT0DknPk3SRpJ83s4u6Xn+3pH+QdFf4Rf4jnO/i8L2Hwi8tSV8J/x+R9Fg4/f/C/4clfVvSQwoCYy72vmheJ+kjXcVcru3p0WVed13/AVTDcscGAH49vvwsAEZAnRdVsdR5hP0AZRRt10lc5/SLk3Riz8fnme/z3qNdzx+KPf9g+PwRBUlXjyrYb/9W0q3h69+StCp8380K4kYnS/otSedI+vvwsz8raVbS/5IkM/spST8o6WmSnilpxsyeGH7eSySdK+l7nHPfK+m6ZdbFQM02nyHpdufcHc65w+FCr+h63RQEwG4Pv/DmcL5XSDoo6XRJ+8OVcJeCFXVEQYTQhSvIKfgRzlQQNVS43ChodoKOrfRHdSy4piX+R7oPmt0bkoXzkMkGVAuVJpRV97a93Lae132hs/wshZDX9VtVSf4eRf1to7rwsOUv6vdFdS2VJNFve87jzdVhyp+1rMuRxOclXeYjCS9vHGnENLqXGY/XRLGWx2PPS8fiOFGLwvi+eKKC/eyIFv8Wzwmf2yfpqQpaNq6W9AQFgbO7JZ0l6XPhPD/jnDuoIAPt9rAMt+lYvOoiSZ91zj3unGtL2iPpueFr05Le5Jw7KknOue8stxIGCZ6tDwsZuSd8Lv76CgUr5G4FmWOPSzogaUpSPVwBHQUrpqbjV+SPhf+fqGDlxANlE7F5o895Qey5+Pewrv+R1V2Pe33vqo88CgAoj+7z4HIVqbzePDrFdwESktf1W1VJ/h5F/W2jblOGLX9Rvy+qa1X4v9e22+9aOI/9gvcqf172x6zLkcTnJV3mXl1R+ZbEdtxvPcWXHcVRVikIcvWaJ94l14rw71D4ntPC51cqCHatUpBQdaGkDeHr5ynoGuzM8LlDChK2zg3fe6akSxS0YDwi6RQzO0PSv0t6rpmdZGZrFMSdovdMSfo5M7vZzP7RzC5cck0o/QPDhQoif70iu3cq+GKPKAimHe5Trkdi74+imvFgWDzK2+8uQV6i8gDyJY8nOgAAimTUevYw70uzLs91AoAyyiqDsjvAFh1TT1Dv42vUijBKmIquxw6H858g6eHYe+8JH18oqaUgPrRVQcvGI2a2OnzunyVdLukqBYG2I865XZI+IelfJX1Y0ud1LH50oqRHnHObJP2Vgq7IljRI8OxeHYvOSUGb0nu7Xj8afrlzFUQFT5B0aligZylIrVuvIOh1uoJo4n4dGzzg7th0FJWMynaijs8oi/d/Jh1bAf2+T16i8gDy5ZDvAiBVeUqh962oF4d5bDpTFUXdZgZR5u/mw6j17GHel2ZdnusEjGPUugbHIaTtzhSXvdR2b13T3XW5qGnnhI415zyiY4GxgwpiRX+voD/9UxT0r/9dSf8iaU5BQOw/w7/nSbrZOfc8Sa8M55Nz7kD4/y3Ouac5534i/Lz/DD//Hkl/F07foCBzbUmDBM/+TdKFZvakMKp3paQbu16XghS4CyW9PPxSVypoT3qfgg7bovasUYDsyQqCYCdKWqcg4rhS0gM6djB5TIsDZFF5Twr/R32iLZc90qvjun6PgTJiO+/tpNh0Euso6wt9n79rXoIaS5Wj32jOSfL5G3R/9lLfragXh0Utty9J3hAo87ov83crK26GlEuezp3jGrUlF8eh9C31W+fh2igvdelR3B+bjloHHtGxpCrp2PdbocUDC9wQzhsd1x9VUGdfEy5rIvzbqyBw9rCCa7a1CppsfkHSZZJ+WNKHJL1U0t+b2SoFo2puUJhFZmYrw+abMrNLFATIdoWfu1NBDEuS/quOBdX6MueW327M7HJJfxZ+qXc7595iZm9SEOG70cyukPSB8Es6BVHDZvieKxV0/LY2fH8UXYz/7xYVioMKAAAAAABAeRxREB9aLvYTJUs9omMDTn5XwUibX5T0TQXxp7MU3ET8O0kvd849amZPkPTlcDkHJf2ac+5WSTKzUyV9UEHLyYfD1/59qQIPFDwDAAAAAAAAqiiPI4kAAAAAAAAAuUDwDAAAAAAAAOiD4BkAAAAAAADQB8EzAAAAAAAAoA+CZwAAAAAAAEAfBM8AAABSYmafCIdDH3T+883sthSLtNRnP+zjcwEAAPLuBN8FAAAAKCvn3OW+ywAAAIDxkHkGAAAwIjP7bTN7ZTj9NjPbHU5famYfNLM7zWxNmFH2dTP7KzPba2a7zGwinPfpZvbvZvbvkl4RW/ZGM/uSmd1qZnvM7MJwOf8RLvvrZvYxMzsptpzPmNktZvYpM1sXPj9lZp8Mn581s+8Jn3+SmX3ezL5qZm/OeNUBAAAUBsEzAACA0c1K2hxOb5J0spmtCp/7bNe8F0p6h3Nuo6QDkn4mfP49kn7DOff9XfP/mqRrnHNPC5d9T/j8UyX9pXPueyUdlPTy8DP/QtLPOueeLundkt4Szn9tuPynS5qR9Jfh89dIajjnvk/SfaN9fQAAgPIjeAYAADC6WyQ93cyeKOlRSZ9XEOjarCCwFvct59ytsfedH/aHdqpzLgq0vT82/+clvd7MXiNpg3OuEz5/t3PuX8LpD0j6UQUBtYslfdrMbpX0O5LOMbOTJT1L0vXh8/9H0rrwvc+W9OEenwsAAIAY+jwDAAAYkXPuMTP7lqSXSPpXSXsk/ZikCyR9vWv2R2PTRyRNLLPsD5nZFyX9lKRPmNmvSrpDkuueVZJJ2uuc+5H4C2FQ70CYvdbzY5YqAwAAAMg8AwAAGNesguaQnw2nf03SV5xzywamnHMHJB0wsx8Nn3pR9JqZPVnSHc65P5f0cUmXhC+dZ2ZRkOwqSZ+T9A1Ja6PnzWyVmW10zh2U9C0z2x4+b2YWNQ/9F0lXdn8uAAAAFiN4BgAAMJ5ZBU0hP++ce0DSIzq+yeZSXirpHWGzSos9/0JJt4XPXyzpfeHz35D0CjP7uqTTFPRbdljSz0r6o3DggVsVNNeUgsDYy8Ln90q6Inz+VeFyvipp/RDlBQAAqBQb4KYoAAAAcsDMzpf0D865i32XBQAAoCrIPAMAAAAAAAD6IPMMAAAAAAAA6IPMMwAAAAAAAKAPgmcAAAAAAABAHwTPAAAAAAAAgD4IngEAAAAAAAB9EDwDAAAAAAAA+iB4BgAAAAAAAPTx/wNWWfFIHXXq3QAAAABJRU5ErkJggg==",
            "text/plain": [
              "<Figure size 1440x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Hubungan antara kecepatan angin pada persewaan sepeda\n",
        "plt.figure(figsize=(20,6))\n",
        "sns.boxplot(x='windspeed', y='counts', data=all_df)\n",
        "plt.title('Hubungan antara kecepatan angin V/S persewaan sepeda')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 746,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        },
        "id": "RGELgyALryIC",
        "outputId": "a2fa2618-d834-47e5-b96a-09ea7f337a37"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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N1xhedy4cYwdO3aV+pg8eTKnnHLKW9onTZrEYYcdtnz57LPPZsyYMSxdurTuvvfbb79VqqWrOEdbkiRJlVq2bBkNDQ00NDS0u915553HPffcw4QJE1hvvfXq6rdv377ce++9nVVqp3JEW5IkSR12yy23MHLkSPbcc08OOeQQ5s6dC8C5557Lsccey/7778+xxx77lpHrli688EJuvfVWbrnlFgYMGMAbb7zBl7/8Zfbaay923313Lr30UqAYAT/wwANpbGxk+PDhwN9H3F966SVGjRrFiBEj2G233bjpppsqfvbtc0RbkiRJ7Xr11VfZY489li8vXLiQxsZGAA444ADuu+8+IoLLL7+cCy64gAsvvBCAxx57jLvvvpsBAwYwadKkNvu/5557eOKJJ5gyZcry0HzFFVewySabcP/997N06VL2339/Ro8eDcADDzzAI4888pYrgPTv358bb7yRjTfemPnz57PPPvvQ2NjYbXPVDdqSJElq14ABA5g6dery5XHjxjF58mSguIzgpz71KWbPns1rr722QvhtbGxkwIABK+1/hx12YNGiRUycOJGPfexjANx222089NBDXH/99QAsXryY6dOns+6667L33nu3epm9zOSss87irrvuok+fPjQ1NTF37lwGDx68Ok+/wwzavdjpp5/OnDlzGDx4MBdccEF3lyNJknqhk08+mS996Us0NjYyadIkzj333OXrNthgg7r6GDRoENdccw2jRo1is8024+CDDyYzueiiizj00ENX2HbSpElt9nvNNdcwb948pkyZQr9+/Rg2bFi33rDHOdq92Jw5c2hqamLOnDndXYokSeqlFi9ezJAhQwC4+uqrO9zPTjvtxA033MAxxxzD1KlTOfTQQ7nkkkt4/fXXAXjyySd5+eWXV1rLVlttRb9+/bjzzjuZOXNmh+vpDJUG7YgYGBHXR8TjETEtIvaNiM0iYmJETC+/b1puGxHxw4iYEREPRcSImn6OL7efHhHHV1mzJEmS6nfuuefyiU98gve85z1sscUWq9XXXnvtxVVXXUVjYyOjRo1i+PDhjBgxgl133ZXPfe5zLFu2rNX9mudgH3300UyePJnddtuN8ePHs/POO69WPasrMrO6ziOuBn6fmZdHxLrA+sBZwMLM/HZEnAFsmplfiYgPAScDHwJGAj/IzJERsRkwGWgAEpgCvCczF7V13IaGhmyeN7Q2O+6442hqamLIkCGMHz++u8uRJEldaNq0aeyyyy7dXUblFixYwIgRI7pk9Lq11zQipmRmq9ctrGxEOyI2Ad4LXAGQma9l5vPA4UDz3xWuBo4oHx8OjM/CfcDAiNgaOBSYmJkLy3A9ERhTVd2SJEnqGZ599ln23XdfTjvttO4upVVVfhhye2AecFVEvJtiJPpUYFBmzi63mQMMKh8PAZ6p2X9W2dZW+woi4iTgJIDtttuu856FJEmS1kjbbLMNTz75ZHeX0aYq52j3BUYAl2TmnsDLwBm1G2Qxb6VT5q5k5mWZ2ZCZDVtuuWVndClJkiR1WJVBexYwKzP/WC5fTxG855ZTQii/P1eubwK2rdl/aNnWVrskSZK0xqosaGfmHOCZiHhn2TQKeAy4GWi+csjxQPO9MW8GjiuvPrIPsLicYvIbYHREbFpeoWR02SZJkiStsaq+Yc3JwDXlFUeeAk6gCPfXRcSJwEzgk+W2EyiuODIDeKXclsxcGBHfBO4vt/tGZi6suG5JkiRptVR6He3MnFrOm949M4/IzEWZuSAzR2Xmjpl5SHNoLq828sXMfEdm7paZk2v6uTIzdyi/rqqyZkmSJHWODTfccIXlcePGMXbs2FXqY/LkyZxyyilvaZ80aRKHHXbY8uWzzz6bMWPGsHTp0rr73m+//VapllXlLdglSZLWAgd+7pud2t/vL/23Tu2vNcuWLaOhoYGGhlYvU73ceeedxz333MOECRNYb7316uq3b9++3HvvvZ1Vaqu8BbskSZK63C233MLIkSPZc889OeSQQ5g7dy5Q3Gny2GOPZf/99+fYY499y8h1SxdeeCG33nort9xyCwMGDOCNN97gy1/+MnvttRe77747l156KVCMgB944IE0NjYyfPhw4O8j7i+99BKjRo1ixIgR7Lbbbtx0001tHm9VOKItSZKkSrz66qvssccey5cXLlxIY2MjAAcccAD33XcfEcHll1/OBRdcwIUXXgjAY489xt13382AAQOYNGlSm/3fc889PPHEE0yZMmV5aL7iiivYZJNNuP/++1m6dCn7778/o0ePBuCBBx7gkUceYfvtt1+hn/79+3PjjTey8cYbM3/+fPbZZx8aGxuX39q9owzakiRJqsSAAQOYOnXq8uVx48YxeXLxMbxZs2bxqU99itmzZ/Paa6+tEH4bGxsZMGDASvvfYYcdWLRoERMnTuRjH/sYALfddhsPPfQQ119/PQCLFy9m+vTprLvuuuy9995vCdkAmclZZ53FXXfdRZ8+fWhqamLu3LkMHjx4dZ6+U0ckSZLU9U4++WTGjh3Lww8/zKWXXsqSJUuWr9tggw3q6mPQoEFMmDCBf/7nf+bOO+8EitB80UUXMXXqVKZOncrTTz+9fES7rX6vueYa5s2bx5QpU5g6dSqDBg1aoZ6OckRbkiSpG42+9sxK+j1rh4+wzsJZlfQN8GQdfSe5wnZzXlrI80te4smFs3hu4XyWbdiXJxfO4qLLfsyry5by5MJZLHj1BV7ts2z5fs+8MI+XX1/yluM1t7PF+nzvqks48h+P4rJrr2aPA/bmP3/wXYbusRP9+vXj6RlPMWjr9kemFy9ezFZbbUW/fv248847mTlzZgdekbcyaEuSJKnLjT39Xzj1M19gk4GbMPLA/Zj1t2c63NfuI/bg3y++kC8c/RnG3/RLmv72DB89+INkJptusTk//unlre7XPAf76KOP5iMf+Qi77bYbDQ0N7Lzzzh2uZYX+M7NTOlqTNDQ0ZPP8n7XZcccdR1NTE0OGDGH8+PHdXY4kSWpFlSPa27x9u0r67ol22mzoCssLFixgxIgRqzR6PW3aNHbZZZcV2iJiSma2ev1B52hLkiRprfLss8+y7777ctppp1V6HKeOSJIkaa2yzTbb8OSTT1Z+HIO2tJpOP/105syZw+DBg7ngggu6uxxJkrSGMGhLq2nOnDk0NTV1dxmSJGkN4xxtSZIkqQIGbUmSJKkCBm1JkiRVYs/t3rnC8g0/v45vnH72KvXx8IN/5rwzvvaW9j/e/Qc+d9Sn39L+1VO/zIzHn2z1+F3NOdqSJElrgbG3/ahT+7t49Bc7tb/WLFu2jN32fDe77fnuuvc5/wf/2WnH7tt39aKyI9qSJEnqcnf830Q+8YGPcMRBY/j0PxzF/OfmAXDRf3yXL3/+VI784D9w+hdObXPkui3HNn6Chx/88/Llb331XD683yhGjRrFvHnFMQ466CCab244f/58hg0bBsC4ceNobGzk/e9/P6NGjVrt5+iItiRJkiqx5NUlHP6+Q5cvL170PO8f8wEA3rPPXlx3281EBL/66S+4/KJLOOObxRSRvzw5nZ//73/Tf8AA/nj3Hzp8/FdefoVd93g3Z51/LtdefCVf//rXufjii9vd54EHHuChhx5is8026/Bxmxm0JUmSVIn+A/pz0+9+s3z5hp9fxyNTHwJgzrOz+ZcT/4l5c5/jtddeZ+jbtl2+3fvHfID+Awas9vH79OnDh/7hIwAcc8wxfPSjH13pPh/4wAc6JWSDU0ckSZLUDc4742sc/dlPc8vdv+Ub3/02ry1dunzdgPVXP2S3JiIA6Nu3L2+++SYAS5YsWWGbDTbYoNOOZ9CWJElSl3vxhRcZtPVgAP7n2l9Vcow333yT39z8vwD8/Oc/54ADDgBg2LBhTJkyBYDrr7++kmODQVuSJEndYOzp/8Kpn/kCH33/hxi4ecemavzhrrt57657Lf968P4pK6xff4P1eeiBqRy2/yjuuOMOvva1Yg74aaedxiWXXMKee+7J/PnzV/u5tCUys7LOu0tDQ0M2f5J0bXbcccfR1NTEkCFDGD9+fHeX02v5OkuSVsfoa8+spN+zdvgI27x9u0r67ol22mzoavcxbdo0dtlllxXaImJKZja0tr0j2pIkSVIFDNqSJElSBQzakiRJUgUM2pIkSb1QAr3xs3jdpSOvpUFbkiSpF5qz5HmWvPiKYbsTZCYLFiygf//+q7Sfd4aUJEnqha6b/Sc+CQzuP5Do7mLWAG/MfXG19u/fvz9Dh67alUsM2pIkSb3Qy28s5apZv+/uMtYYtx35711+TKeOSJIkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFag0aEfEXyPi4YiYGhGTy7bNImJiREwvv29atkdE/DAiZkTEQxExoqaf48vtp0fE8VXWLEmSJHWGrhjRPjgz98jMhnL5DOD2zNwRuL1cBvggsGP5dRJwCRTBHDgHGAnsDZzTHM4lSZKkNVV3TB05HLi6fHw1cERN+/gs3AcMjIitgUOBiZm5MDMXAROBMV1csyRJkrRKqg7aCdwWEVMi4qSybVBmzi4fzwEGlY+HAM/U7DurbGurfQURcVJETI6IyfPmzevM5yBJkiStsr4V939AZjZFxFbAxIh4vHZlZmZEZGccKDMvAy4DaGho6JQ+JUmSpI6qdEQ7M5vK788BN1LMsZ5bTgmh/P5cuXkTsG3N7kPLtrbaJUmSpDVWZSPaEbEB0CczXywfjwa+AdwMHA98u/x+U7nLzcDYiLiW4oOPizNzdkT8BvhWzQcgRwNnVlW3ut/oa3vWj/eNF+cD0PTi/B5T+21H/nt3lyBJUq9X5dSRQcCNEdF8nJ9n5v9FxP3AdRFxIjAT+GS5/QTgQ8AM4BXgBIDMXBgR3wTuL7f7RmYurLBuSZIkabVVFrQz8yng3a20LwBGtdKewBfb6OtK4MrOrlGSJEmqineGlCRJkipg0JYkSZIqYNCWJEmSKmDQliRJkipg0JYkSZIqYNCWJEmSKmDQliRJkipg0JYkSZIqYNCWJEmSKmDQliRJkipg0JYkSZIqYNCWJEmSKmDQliRJkipg0JYkSZIqYNCWJEmSKmDQliRJkirQt7sLkCStGUZfe2Z3l9Dr3Xbkv3d3CZK6kCPakiRJUgUM2pIkSVIFDNqSJElSBQzakiRJUgUM2pIkSVIFDNqSJElSBQzakiRJUgUM2pIkSVIFDNqSJElSBQzakiRJUgW8BfsqOvBz3+zuEurW77mFBDDruYU9qu4BB3d3BZIkSavPEW1JkiSpAgZtSZIkqQIGbUmSJKkCBm1JkiSpAgZtSZIkqQIGbUmSJKkCBm1JkiSpAgZtSZIkqQIGbUmSJKkC3hlSWl0brbfid0mSJAza0mpb50M7d3cJkiRpDeTUEUmSJKkCBm1JkiSpAnVNHYmI/YBhtdtn5viKapIkSZJ6vJWOaEfET4HvAAcAe5VfDfUeICLWiYgHI+LX5fL2EfHHiJgREb+MiHXL9vXK5Rnl+mE1fZxZtj8REYeu2lOUJEmSul49I9oNwPDMzA4e41RgGrBxufwfwPcy89qI+C/gROCS8vuizNwhIo4st/tURAwHjgTeBWwD/DYidsrMNzpYjyRJklS5euZoPwIM7kjnETEU+DBwebkcwPuB68tNrgaOKB8fXi5Trh9Vbn84cG1mLs3Mp4EZwN4dqUeSJEnqKvWMaG8BPBYRfwKWNjdmZmMd+34fOB3YqFzeHHg+M5eVy7OAIeXjIcAzZd/LImJxuf0Q4L6aPmv3WS4iTgJOAthuu+3qKE2SJEmqTj1B+9yOdBwRhwHPZeaUiDioI32sisy8DLgMoKGhoaPTXCRJkqROsdKgnZm/62Df+wONEfEhoD/FHO0fAAMjom85qj0UaCq3bwK2BWZFRF9gE2BBTXuz2n0kSZKkNVI9Vx3ZJyLuj4iXIuK1iHgjIl5Y2X6ZeWZmDs3MYRQfZrwjM48G7gQ+Xm52PHBT+fjmcply/R3lBzBvBo4sr0qyPbAj8KdVeI6SJElSl6tn6sjFFEH5VxRXIDkO2Gk1jvkV4NqIOA94ELiibL8C+GlEzAAWlsckMx+NiOuAx4BlwBe94ogkSZLWdHXdsCYzZ0TEOmXAvSoiHgTOrPcgmTkJmFQ+fopWrhqSmUuAT7Sx//nA+fUeT5IkSepu9QTtV8qbykyNiAuA2XjrdkmSJKld9QTmY8vtxgIvU3ww8WNVFiVJkiT1dPVcdWRm+XAJ8PVqy5EkSZJ6h5UG7YjYEfh3YDjFZfoAyMy3V1iXJEmS1KPVM3XkKuASiit+HAyMB35WZVGSJElST1dP0B6QmbcDkZkzM/Nc4MPVliVJkiT1bPVcdWRpRPQBpkfEWIq7Mm5YbVmSJElSz1bPiPapwPrAKcB7gGP4+x0cJUmSJLWinhHthZn5EvAScELF9UiSJEm9Qj1B+8qIGArcD/weuCszH662LEmSJKlnq+c62u8r7wy5F3AQ8L8RsWFmblZ1cZIkSVJPVc91tA8ADiy/BgK/phjZliRJktSGeqaOTAKmUNy0ZkJmvlZpRZIkSVIvUE/Q3gLYH3gvcEpEvAn8ITP/rdLKJEmSpB6snjnaz0fEU8C2wFBgP6Bf1YVJkiRJPVk9c7SfAh4H7qa4FfsJTh+RJEmS2lfP1JEdMvPNyiuRJEmSepF67gy5Q0TcHhGPAETE7hFxdsV1SZIkST1aPUH7J8CZwOsAmfkQcGSVRUmSJEk9XT1Be/3M/FOLtmVVFCNJkiT1FvUE7fkR8Q4gASLi48DsSquSJEmSerh6Pgz5ReAyYOeIaAKeBo6utCpJkiSph6snaM/MzEMiYgOgT2a+WHVRkiRJUk9Xz9SR6RHxn8B2hmxJkiSpPvUE7XcDTwJXRMR9EXFSRGxccV2SJElSj7bSoJ2ZL2bmTzJzP+ArwDnA7Ii4OiJ2qLxCSZIkqQdaadCOiHUiojEibgS+D1wIvB24BZhQbXmSJElSz1TPhyGnA3cC/5mZ99a0Xx8R762mLEmSJKlnqydo756ZL7W2IjNP6eR6JEmSpF6hnqA9ICJOAYbVbp+Zn6mqKEmSJKmnqydo3wT8Hvgt8Ea15UiSJEm9Qz1Be/3M/ErllUiSJEm9SD3X0f51RHyo8kokSZKkXqSeoH0qRdheEhEvRMSLEfFC1YVJkiRJPdlKp45k5kZdUYgkSZLUm9Rzw5qIiGMi4t/K5W0jYu/qS5MkSZJ6rnqmjvwY2Bf4x3L5JeBHlVUkSZIk9QL1XHVkZGaOiIgHATJzUUSsW3FdkiRJUo9Wz4j26xGxDpAAEbEl8GalVUmSJEk9XD1B+4fAjcBWEXE+cDfwrUqrkiRJknq4eq46ck1ETAFGAQEckZnTKq9MkiRJ6sHaDNoRMRK4DHgH8DBwYmY+1lWFSZIkST1Ze1NHfgScBmwOfBf43qp0HBH9I+JPEfHniHg0Ir5etm8fEX+MiBkR8cvmD1ZGxHrl8oxy/bCavs4s25+IiENX9UlKkiRJXa29oN0nMydm5tLM/BWw5Sr2vRR4f2a+G9gDGBMR+wD/AXwvM3cAFgEnltufCCwq279XbkdEDAeOBN4FjAF+XH44U5IkSVpjtRe0B0bER5u/WlluVxZeKhf7lV8JvB+4vmy/GjiifHx4uUy5flRERNl+bRn4nwZmAN4wR5IkSWu09j4M+TvgI20sJ3DDyjovR56nADtQTEX5C/B8Zi4rN5kFDCkfDwGeAcjMZRGxmGLayhDgvppua/epPdZJwEkA22233cpKkyRJkirVZtDOzBNWt/PMfAPYIyIGUlwicOfV7bOdY11G8eFNGhoasqrjSJIkSfWo5zraqy0znwfupLiV+8CIaA74Q4Gm8nETsC1AuX4TYEFteyv7SJIkSWukyoJ2RGxZjmQTEQOADwDTKAL3x8vNjgduKh/fXC5Trr8jM7NsP7K8Ksn2wI7An6qqW5IkSeoMK71hzWrYGri6nKfdB7guM38dEY8B10bEecCDwBXl9lcAP42IGcBCiiuNkJmPRsR1wGPAMuCL5ZQUSZIkaY1VV9COiP2AYbXbZ+b49vbJzIeAPVtpf4pWrhqSmUuAT7TR1/nA+fXUKkmSJK0JVhq0I+KnFHeHnAo0jyQn0G7QliRJktZm9YxoNwDDy/nSkiRJkupQz4chHwEGV12IJEmS1Ju0OaIdEbdQTBHZCHgsIv5EcVt1ADKzsfryJEmSpJ6pvakj3+myKiRJkqRepr07Q/6uKwuRJEmSepOVztGOiH0i4v6IeCkiXouINyLiha4oTpIkSeqp6vkw5MXAUcB0YADwWeBHVRYlSZIk9XR13YI9M2cA62TmG5l5FTCm2rIkSZKknq2e62i/EhHrAlMj4gJgNnUGdEmSJGltVU9gPhZYBxgLvAxsC3ysyqIkSZKknm6lI9qZObN8+Crw9WrLkSRJknqH9m5Y8zDFDWtalZm7V1KRJEmS1Au0N6J9WJdVIUmSJPUy7d2wZmbtckRs3N72kiRJkv5upcE5Ij5HMTd7CX+fSpLA2yusS5IkSerR6hmhPg3YNTPnV12MJEmS1FvUc3m/vwCvVF2IJEmS1JvUM6J9JnBvRPwRWNrcmJmnVFaVOkX27b/Cd0mSJHWdeoL2pcAdwMPAm9WWo860bMi7u7sESZKktVY9QbtfZn6p8kokSZKkXqSeOdq3RsRJEbF1RGzW/FV5ZZIkSVIPVs+I9lHl9zNr2ry8nyRJktSOlQbtzNy+KwqRJEmSepN6blhzXGvtmTm+88uRJEmSeod6po7sVfO4PzAKeAAwaEuSJEltqGfqyMm1yxExELi2qoIkSZKk3qCeq4609DLgvG1JkiSpHfXM0b6F4iojAOsAw4HrqixKkiRJ6unqmaP9Hf4etJcBMzOzqbqSJEmSpJ6vzaAdES9SBOxosSojYinwF+CrmXl7hfVJkiRJPVKbQTszN2prXUSsA+wKXFN+lyRJklSjIx+GJDPfyMw/Axd1cj2SJElSr9ChoN0sMy/trEIkSZKk3mS1grYkSZKk1hm0JUmSpAoYtCVJkqQKGLQlSZKkChi0JUmSpAoYtCVJkqQKGLQlSZKkChi0JUmSpApUFrQjYtuIuDMiHouIRyPi1LJ9s4iYGBHTy++blu0RET+MiBkR8VBEjKjp6/hy++kRcXxVNUuSJEmdpcoR7WXAv2bmcGAf4IsRMRw4A7g9M3cEbi+XAT4I7Fh+nQRcAkUwB84BRgJ7A+c0h3NJkiRpTVVZ0M7M2Zn5QPn4RWAaMAQ4HLi63Oxq4Ijy8eHA+CzcBwyMiK2BQ4GJmbkwMxcBE4ExVdUtSZIkdYYumaMdEcOAPYE/AoMyc3a5ag4wqHw8BHimZrdZZVtb7ZIkSdIaq/KgHREbAv8N/HNmvlC7LjMTyE46zkkRMTkiJs+bN68zupQkSZI6rNKgHRH9KEL2NZl5Q9k8t5wSQvn9ubK9Cdi2ZvehZVtb7SvIzMsysyEzG7bccsvOfSKSJEnSKqryqiMBXAFMy8zv1qy6GWi+csjxwE017ceVVx/ZB1hcTjH5DTA6IjYtPwQ5umyTJEmS1lh9K+x7f+BY4OGImFq2nQV8G7guIk4EZgKfLNdNAD4EzABeAU4AyMyFEfFN4P5yu29k5sIK65YkSZJWW2VBOzPvBqKN1aNa2T6BL7bR15XAlZ1XnSRJklQt7wwpSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVwKAtSZIkVcCgLUmSJFXAoC1JkiRVoLKgHRFXRsRzEfFITdtmETExIqaX3zct2yMifhgRMyLioYgYUbPP8eX20yPi+KrqlSRJkjpTlSPa44AxLdrOAG7PzB2B28tlgA8CO5ZfJwGXQBHMgXOAkcDewDnN4VySJElak1UWtDPzLmBhi+bDgavLx1cDR9S0j8/CfcDAiNgaOBSYmJkLM3MRMJG3hndJkiRpjdPVc7QHZebs8vEcYFD5eAjwTM12s8q2ttolSZKkNVq3fRgyMxPIzuovIk6KiMkRMXnevHmd1a0kSZLUIV0dtOeWU0Iovz9XtjcB29ZsN7Rsa6v9LTLzssxsyMyGLbfcstMLlyRJklZFVwftm4HmK4ccD9xU035cefWRfYDF5RST3wCjI2LT8kOQo8s2SZIkaY3Wt6qOI+IXwEHAFhExi+LqId8GrouIE4GZwCfLzScAHwJmAK8AJwBk5sKI+CZwf7ndNzKz5QcsJUmSpDVOZUE7M49qY9WoVrZN4Itt9HMlcGUnliZJkiRVzjtDSpIkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFTBoS5IkSRUwaEuSJEkVMGhLkiRJFegxQTsixkTEExExIyLO6O56JEmSpPb0iKAdEesAPwI+CAwHjoqI4d1blSRJktS2HhG0gb2BGZn5VGa+BlwLHN7NNUmSJElt6ilBewjwTM3yrLJNkiRJWiNFZnZ3DSsVER8HxmTmZ8vlY4GRmTm2ZpuTgJPKxXcCT3R5oeosWwDzu7sIaS3kuSd1D8+9nu1tmbllayv6dnUlHdQEbFuzPLRsWy4zLwMu68qiVI2ImJyZDd1dh7S28dyTuofnXu/VU6aO3A/sGBHbR8S6wJHAzd1ckyRJktSmHjGinZnLImIs8BtgHeDKzHy0m8uSJEmS2tQjgjZAZk4AJnR3HeoSTgGSuofnntQ9PPd6qR7xYUhJkiSpp+kpc7QlSZKkHsWgrW4TEWMi4omImBERZ7Syfr2I+GW5/o8RMawbypR6vIi4MiKei4hHatr+MyIej4iHIuLGiBjYxr7tnqeS2tbauVe2n1yef49GxAVt7Ou51wsYtNUtImId4EfAB4HhwFERMbzFZicCizJzB+B7wH90bZVSrzEOGNOibSKwa2buDjwJnNlypzrPU0ltG0eLcy8iDqa4u/W7M/NdwHda7uS513sYtNVd9gZmZOZTmfkacC3FPzy1DgeuLh9fD4yKiOjCGqVeITPvAha2aLstM5eVi/dR3J+gpXrOU0ltaO3cA74AfDszl5bbPNfKrp57vYRBW91lCPBMzfKssq3VbcpAsBjYvEuqk9YunwFubaW9nvNU0qrZCTiwnBL5u4jYq5VtPPd6iR5zeT9JUueLiK8Cy4BrursWaS3RF9gM2AfYC7guIt6eXgauV3JEW92lCdi2Znlo2dbqNhHRF9gEWNAl1UlrgYj4NHAYcHQb/8nXc55KWjWzgBuy8CfgTWCLFtt47vUSBm11l/uBHSNi+4hYFzgSuLnFNjcDx5ePPw7c4W/8UueIiDHA6UBjZr7Sxmb1nKeSVs3/AAcDRMROwLrA/BbbeO71EgZtdYtyzvVY4DfANOC6zHw0Ir4REY3lZlcAm0fEDOBLgJc3kjogIn4B/AF4Z0TMiogTgYuBjYCJETE1Iv6r3HabiJgAbZ+n3fIkpB6ojXPvSuDt5SX/rgWOz8z03OudvDOkJEmSVAFHtCVJkqQKGLQlSZKkChi0JUmSpAoYtCVJkqQKGLQlSZKkChi0JWktEREvdXcNkrQ2MWhLkiRJFTBoS9JaJCI2jIjbI+KBiHg4Ig4v24dFxOMRMS4inoyIayLikIi4JyKmR8Te3V27JPU03rBGktYS5dSRgcD6mflCRGwB3AfsCLwNmAHsCTxKcQvoPwMnAo3ACZl5RDeULUk9Vt/uLkCS1KUC+FZEvBd4ExgCDCrXPZ2ZDwNExKPA7eWtoR8GhnVHsZLUkxm0JWntcjSwJfCezHw9Iv4K9C/XLa3Z7s2a5Tfx/wtJWmXO0ZaktcsmwHNlyD6YYsqIJKkCjlBI0logIvpSjFBfA9xSTgeZDDzerYVJUi/mhyElaS0QEe8GfpKZXj1EkrqIU0ckqZeLiM8DvwDO7u5aJGlt4oi2JEmSVAFHtCVJkqQKGLQlSZKkChi0JUmSpAoYtCVJkqQKGLQlSZKkChi0JUmSpAr8f+CB2UPu7FoKAAAAAElFTkSuQmCC",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Tren harian peminjaman sepeda tergantung pada hari kerja (workingday)\n",
        "plt.figure(figsize=(12, 6))\n",
        "\n",
        "sns.barplot(x='hour', y='counts', hue='workingday', data=all_df, palette='viridis')\n",
        "\n",
        "plt.title('Tren Harian Peminjaman Sepeda tergantung pada Hari Kerja')\n",
        "plt.xlabel('Jam')\n",
        "plt.ylabel('Jumlah Penyewaan')\n",
        "\n",
        "# Tampilkan legenda\n",
        "plt.legend(title='Hari Kerja', loc='upper right')\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 737,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 589
        },
        "id": "qSI1ndferyFn",
        "outputId": "af15b7fb-7f84-45b0-8800-73954b147172"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "Analisis tren dari waktu ke waktu:\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<AxesSubplot:title={'center':'Tren Penyewaan Sepeda dari Waktu ke Waktu'}, xlabel='dteday'>"
            ]
          },
          "execution_count": 737,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Analisis Tren Waktu\n",
        "print(\"\\nAnalisis tren dari waktu ke waktu:\")\n",
        "all_df.set_index('dteday')['counts'].plot(figsize=(12, 6), title='Tren Penyewaan Sepeda dari Waktu ke Waktu')\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z66Ddw26iqRm"
      },
      "source": [
        "## Analysis Lanjutan menggunakan K-Means Clustering"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 738,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "Q7VTqp-Gf9dw",
        "outputId": "3473d9cb-2815-424b-b114-b30c45f78ffd"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Mengelompokkan data ke dalam beberapa cluster berdasarkan kemiripan fitur menggunakan K-Means CLustering\n",
        "X = all_df[['temp', 'hum']]\n",
        "\n",
        "# Normalisasi fitur\n",
        "X_normalized = (X - X.mean()) / X.std()\n",
        "\n",
        "# Menentukan jumlah cluster (k)\n",
        "k = 3\n",
        "\n",
        "# Inisialisasi centroid secara acak\n",
        "np.random.seed(42)\n",
        "centroids = X_normalized.sample(k).to_numpy()\n",
        "\n",
        "# Melakukan iterasi hingga konvergensi\n",
        "max_iter = 100\n",
        "for _ in range(max_iter):\n",
        "\n",
        "    # Menghitung jarak antara setiap titik dan centroid\n",
        "    distances = np.linalg.norm(X_normalized.values[:, np.newaxis] - centroids, axis=2)\n",
        "\n",
        "    # Menentukan cluster untuk setiap titik berdasarkan jarak terdekat\n",
        "    labels = np.argmin(distances, axis=1)\n",
        "\n",
        "    # Memperbarui centroid berdasarkan rata-rata titik dalam setiap cluster\n",
        "    new_centroids = np.array([X_normalized[labels == i].mean(axis=0) for i in range(k)])\n",
        "\n",
        "    # Memeriksa konvergensi\n",
        "    if np.all(centroids == new_centroids):\n",
        "        break\n",
        "\n",
        "    centroids = new_centroids\n",
        "\n",
        "# Menambahkan kolom cluster ke dataframe\n",
        "day_df['cluster'] = labels\n",
        "\n",
        "# Visualisasi\n",
        "plt.scatter(X_normalized['temp'], X_normalized['hum'], c=day_df['cluster'], cmap='viridis')\n",
        "plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')\n",
        "plt.xlabel('Normalized Temperature')\n",
        "plt.ylabel('Normalized Humidity')\n",
        "plt.title('K-Means Clustering on day_df')\n",
        "plt.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EpFBRqX1i3KH"
      },
      "source": [
        "## Pertanyaan"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HZxOiQ6n8DC2"
      },
      "source": [
        "### Pertanyaan 1: Bagaimana pola penggunaan penyewaan sepeda pada hari kerja dibandingkan dengan hari libur?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 739,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "1swJUdAD8DC2",
        "outputId": "863dec74-36fa-4738-e690-744a056999ca"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 576x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Bagaimana pola penggunaan penyewaan sepeda pada hari kerja dibandingkan dengan hari libur?\n",
        "day_type_counts = all_df['workingday'].value_counts()\n",
        "\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x=day_type_counts.index, y=day_type_counts.values, palette='viridis')\n",
        "\n",
        "plt.xlabel('Hari')\n",
        "plt.ylabel('Jumlah Penyewaan')\n",
        "plt.title('Pola Penggunaan Penyewaan Sepeda pada Hari Kerja vs Hari Libur')\n",
        "\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DgHI7CiU8DC2"
      },
      "source": [
        "### Pertanyaan 2: Apakah penggunaan meningkat saat cuaca cerah atau menurun saat hujan?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 741,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "Go0lCsvO8DC2",
        "outputId": "43198107-3125-4e45-bbda-38387c07701f"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Apakah penggunaan meningkat saat cuaca cerah atau menurun saat hujan?\n",
        "\n",
        "all_df.groupby('weathersit').size().sort_values(ascending=True).plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))\n",
        "plt.gca().spines['top'].set_visible(False)\n",
        "plt.gca().spines['right'].set_visible(False)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_WeHlCeX8DC2"
      },
      "source": [
        "## Conclusion/Kesimpulan"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZTcyR48Y8DC2"
      },
      "source": [
        "- Pada Hari Libur terdapat peningkatan penggunaan/penyewaan sepeda, sedangkan pada Hari Kerja mengalami penurunan.\n",
        "- Ya, ada penurunan penggunaan/penyewaan pada saat hujan, hal tersebut bisa terlihat pada diagram batang pada visualisasi data diatas."
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.13"
    },
    "orig_nbformat": 4,
    "vscode": {
      "interpreter": {
        "hash": "972b3bf27e332e87b5379f2791f6ef9dfc79c71018c370b0d7423235e20fe4d7"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
