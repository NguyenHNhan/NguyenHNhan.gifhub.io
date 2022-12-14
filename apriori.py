{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NguyenHNhan/NguyenHNhan.gifhub.io/blob/main/B%E1%BA%A3n_sao_c%E1%BB%A7a_Colaboratory_ch%C3%A0o_m%E1%BB%ABng_b%E1%BA%A1n!.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "VucY3OMKE3dz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "2CRI7879E7XE",
        "outputId": "38f4b03e-fbc3-4f5b-91fc-b86282c4ad58",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "import pandas as pd\n",
        "from mlxtend.frequent_patterns import apriori, association_rules"
      ],
      "metadata": {
        "id": "RBQJx68WFAUw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_excel('/content/drive/MyDrive/KPDL/T8/Online Retail.xlsx')\n",
        "data.head()"
      ],
      "metadata": {
        "id": "W4eHUxo1FB-I",
        "outputId": "ff9f32b4-4712-43b2-cc38-6ebb1798eb08",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  InvoiceNo StockCode                          Description  Quantity  \\\n",
              "0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   \n",
              "1    536365     71053                  WHITE METAL LANTERN         6   \n",
              "2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   \n",
              "3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   \n",
              "4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   \n",
              "\n",
              "          InvoiceDate  UnitPrice  CustomerID         Country  \n",
              "0 2010-12-01 08:26:00       2.55     17850.0  United Kingdom  \n",
              "1 2010-12-01 08:26:00       3.39     17850.0  United Kingdom  \n",
              "2 2010-12-01 08:26:00       2.75     17850.0  United Kingdom  \n",
              "3 2010-12-01 08:26:00       3.39     17850.0  United Kingdom  \n",
              "4 2010-12-01 08:26:00       3.39     17850.0  United Kingdom  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b64517f2-726a-41b6-8150-85acbde8ee3d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>InvoiceNo</th>\n",
              "      <th>StockCode</th>\n",
              "      <th>Description</th>\n",
              "      <th>Quantity</th>\n",
              "      <th>InvoiceDate</th>\n",
              "      <th>UnitPrice</th>\n",
              "      <th>CustomerID</th>\n",
              "      <th>Country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>536365</td>\n",
              "      <td>85123A</td>\n",
              "      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>\n",
              "      <td>6</td>\n",
              "      <td>2010-12-01 08:26:00</td>\n",
              "      <td>2.55</td>\n",
              "      <td>17850.0</td>\n",
              "      <td>United Kingdom</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>536365</td>\n",
              "      <td>71053</td>\n",
              "      <td>WHITE METAL LANTERN</td>\n",
              "      <td>6</td>\n",
              "      <td>2010-12-01 08:26:00</td>\n",
              "      <td>3.39</td>\n",
              "      <td>17850.0</td>\n",
              "      <td>United Kingdom</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>536365</td>\n",
              "      <td>84406B</td>\n",
              "      <td>CREAM CUPID HEARTS COAT HANGER</td>\n",
              "      <td>8</td>\n",
              "      <td>2010-12-01 08:26:00</td>\n",
              "      <td>2.75</td>\n",
              "      <td>17850.0</td>\n",
              "      <td>United Kingdom</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>536365</td>\n",
              "      <td>84029G</td>\n",
              "      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>\n",
              "      <td>6</td>\n",
              "      <td>2010-12-01 08:26:00</td>\n",
              "      <td>3.39</td>\n",
              "      <td>17850.0</td>\n",
              "      <td>United Kingdom</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>536365</td>\n",
              "      <td>84029E</td>\n",
              "      <td>RED WOOLLY HOTTIE WHITE HEART.</td>\n",
              "      <td>6</td>\n",
              "      <td>2010-12-01 08:26:00</td>\n",
              "      <td>3.39</td>\n",
              "      <td>17850.0</td>\n",
              "      <td>United Kingdom</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b64517f2-726a-41b6-8150-85acbde8ee3d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b64517f2-726a-41b6-8150-85acbde8ee3d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b64517f2-726a-41b6-8150-85acbde8ee3d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.columns"
      ],
      "metadata": {
        "id": "l3Ck4VNLFYZd",
        "outputId": "1b7b287b-0f1c-42d4-a8f3-81b96504360a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',\n",
              "       'UnitPrice', 'CustomerID', 'Country'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.Country.unique()"
      ],
      "metadata": {
        "id": "klj7TWk2FbJ3",
        "outputId": "3b411d53-75f4-41c6-c2dd-42301d1e750f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['United Kingdom', 'France', 'Australia', 'Netherlands', 'Germany',\n",
              "       'Norway', 'EIRE', 'Switzerland', 'Spain', 'Poland', 'Portugal',\n",
              "       'Italy', 'Belgium', 'Lithuania', 'Japan', 'Iceland',\n",
              "       'Channel Islands', 'Denmark', 'Cyprus', 'Sweden', 'Austria',\n",
              "       'Israel', 'Finland', 'Bahrain', 'Greece', 'Hong Kong', 'Singapore',\n",
              "       'Lebanon', 'United Arab Emirates', 'Saudi Arabia',\n",
              "       'Czech Republic', 'Canada', 'Unspecified', 'Brazil', 'USA',\n",
              "       'European Community', 'Malta', 'RSA'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data['Description'] = data[ 'Description'].str.strip()"
      ],
      "metadata": {
        "id": "h6cjfQtIFcuT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True)"
      ],
      "metadata": {
        "id": "aGTGQBZZFfnO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[ 'InvoiceNo'] = data[ 'InvoiceNo' ].astype('str')"
      ],
      "metadata": {
        "id": "mU0YIgkIFhQF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = data[~data[ 'InvoiceNo' ].str.contains(\"C\")]"
      ],
      "metadata": {
        "id": "_gF_RarIFimh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "basket_France = (data[data['Country'] ==\"France\"]\n",
        "      .groupby(['InvoiceNo','Description'])['Quantity']\n",
        "      .sum().unstack().reset_index().fillna(0)\n",
        "      .set_index('InvoiceNo'))"
      ],
      "metadata": {
        "id": "sfqOvMcRFlY7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "basket_UK = (data[data['Country'] ==\"United Kingdom\"]\n",
        "      .groupby(['InvoiceNo','Description'])['Quantity']\n",
        "      .sum().unstack().reset_index().fillna(0)\n",
        "      .set_index('InvoiceNo'))"
      ],
      "metadata": {
        "id": "SDHpc3XuFlxx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "basket_Por = (data[data['Country'] ==\"Portugal\"]\n",
        "      .groupby(['InvoiceNo','Description'])['Quantity']\n",
        "      .sum().unstack().reset_index().fillna(0)\n",
        "      .set_index('InvoiceNo'))\n",
        "basket_Sweden = (data[data['Country'] ==\"Sweden\"]\n",
        "      .groupby(['InvoiceNo','Description'])['Quantity']\n",
        "      .sum().unstack().reset_index().fillna(0)\n",
        "      .set_index('InvoiceNo'))"
      ],
      "metadata": {
        "id": "e3mWhyv-FrBE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def hot_encode(x):\n",
        "  if(x<= 0):\n",
        "    return 0\n",
        "  if(x>= 1):\n",
        "    return 1\n",
        "\n",
        "basket_encoded = basket_France.applymap(hot_encode)\n",
        "basket_France = basket_encoded\n",
        "\n",
        "basket_encoded = basket_Por.applymap(hot_encode)\n",
        "basket_Por = basket_encoded\n",
        "\n",
        "basket_encoded = basket_UK.applymap(hot_encode)\n",
        "basket_UK = basket_encoded\n",
        "\n",
        "basket_encoded = basket_Sweden.applymap (hot_encode)\n",
        "basket_Sweden = basket_encoded"
      ],
      "metadata": {
        "id": "GcAOD_JeFxUE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "frq_items = apriori(basket_France, min_support = 0.05, use_colnames = True)\n",
        "rules = association_rules(frq_items, metric =\"lift\", min_threshold = 1)\n",
        "\n",
        "rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])\n",
        "print(rules.head())\n"
      ],
      "metadata": {
        "id": "2V7XsBgcF5FY",
        "outputId": "6e901341-b6cb-4879-ab0a-56461deacccb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                           antecedents  \\\n",
            "44                        (JUMBO BAG WOODLAND ANIMALS)   \n",
            "258  (RED TOADSTOOL LED NIGHT LIGHT, PLASTERS IN TI...   \n",
            "270  (RED TOADSTOOL LED NIGHT LIGHT, PLASTERS IN TI...   \n",
            "302  (SET/20 RED RETROSPOT PAPER NAPKINS, SET/6 RED...   \n",
            "300  (SET/6 RED SPOTTY PAPER PLATES, SET/20 RED RET...   \n",
            "\n",
            "                         consequents  antecedent support  consequent support  \\\n",
            "44                         (POSTAGE)            0.076531            0.765306   \n",
            "258                        (POSTAGE)            0.051020            0.765306   \n",
            "270                        (POSTAGE)            0.053571            0.765306   \n",
            "302  (SET/6 RED SPOTTY PAPER PLATES)            0.102041            0.127551   \n",
            "300    (SET/6 RED SPOTTY PAPER CUPS)            0.102041            0.137755   \n",
            "\n",
            "      support  confidence      lift  leverage  conviction  \n",
            "44   0.076531       1.000  1.306667  0.017961         inf  \n",
            "258  0.051020       1.000  1.306667  0.011974         inf  \n",
            "270  0.053571       1.000  1.306667  0.012573         inf  \n",
            "302  0.099490       0.975  7.644000  0.086474   34.897959  \n",
            "300  0.099490       0.975  7.077778  0.085433   34.489796  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "frq_items = apriori(basket_UK, min_support = 0.01, use_colnames = True) \n",
        "rules = association_rules(frq_items, metric =\"lift\", min_threshold = 1) \n",
        "rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) \n",
        "print(rules.head()) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bj3q8Y_DPSzI",
        "outputId": "74d587b0-6e04-46c2-f14c-15ce4b40609a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                       antecedents             consequents  \\\n",
            "116           (BEADED CRYSTAL HEART PINK ON STICK)        (DOTCOM POSTAGE)   \n",
            "2018  (JAM MAKING SET PRINTED, SUKI  SHOULDER BAG)        (DOTCOM POSTAGE)   \n",
            "2296         (HERB MARKER MINT, HERB MARKER THYME)  (HERB MARKER ROSEMARY)   \n",
            "2300   (HERB MARKER PARSLEY, HERB MARKER ROSEMARY)     (HERB MARKER THYME)   \n",
            "2301      (HERB MARKER PARSLEY, HERB MARKER THYME)  (HERB MARKER ROSEMARY)   \n",
            "\n",
            "      antecedent support  consequent support   support  confidence       lift  \\\n",
            "116             0.011036            0.037928  0.010768    0.975728  25.725872   \n",
            "2018            0.011625            0.037928  0.011196    0.963134  25.393807   \n",
            "2296            0.010714            0.012375  0.010232    0.955000  77.173095   \n",
            "2300            0.011089            0.012321  0.010553    0.951691  77.240055   \n",
            "2301            0.011089            0.012375  0.010553    0.951691  76.905682   \n",
            "\n",
            "      leverage  conviction  \n",
            "116   0.010349   39.637371  \n",
            "2018  0.010755   26.096206  \n",
            "2296  0.010099   21.947227  \n",
            "2300  0.010417   20.444951  \n",
            "2301  0.010416   20.443842  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "frq_items = apriori(basket_Por, min_support = 0.05, use_colnames = True)\n",
        "rules = association_rules(frq_items, metric =\"lift\", min_threshold = 1)\n",
        "\n",
        "rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])\n",
        "print(rules.head())"
      ],
      "metadata": {
        "id": "jtqnzJ8WPNIL",
        "outputId": "3d6e1e5b-8c23-42a6-fa68-5fa900ba2ca1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                             antecedents                          consequents  \\\n",
            "1170    (SET 12 COLOUR PENCILS SPACEBOY)   (SET 12 COLOUR PENCILS DOLLY GIRL)   \n",
            "1171  (SET 12 COLOUR PENCILS DOLLY GIRL)     (SET 12 COLOUR PENCILS SPACEBOY)   \n",
            "1172  (SET OF 4 KNICK KNACK TINS LONDON)   (SET 12 COLOUR PENCILS DOLLY GIRL)   \n",
            "1173  (SET 12 COLOUR PENCILS DOLLY GIRL)   (SET OF 4 KNICK KNACK TINS LONDON)   \n",
            "1174  (SET 12 COLOUR PENCILS DOLLY GIRL)  (SET OF 4 KNICK KNACK TINS POPPIES)   \n",
            "\n",
            "      antecedent support  consequent support   support  confidence       lift  \\\n",
            "1170            0.051724            0.051724  0.051724         1.0  19.333333   \n",
            "1171            0.051724            0.051724  0.051724         1.0  19.333333   \n",
            "1172            0.051724            0.051724  0.051724         1.0  19.333333   \n",
            "1173            0.051724            0.051724  0.051724         1.0  19.333333   \n",
            "1174            0.051724            0.051724  0.051724         1.0  19.333333   \n",
            "\n",
            "      leverage  conviction  \n",
            "1170  0.049049         inf  \n",
            "1171  0.049049         inf  \n",
            "1172  0.049049         inf  \n",
            "1173  0.049049         inf  \n",
            "1174  0.049049         inf  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "frq_items = apriori(basket_Sweden, min_support = 0.05, use_colnames = True)\n",
        "rules = association_rules(frq_items, metric =\"lift\", min_threshold = 1)\n",
        "\n",
        "rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])\n",
        "print(rules.head())"
      ],
      "metadata": {
        "id": "xLruLUAOOt-M",
        "outputId": "78545348-7661-47af-ab99-2ffe0c36958a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                        antecedents                        consequents  \\\n",
            "0     (12 PENCILS SMALL TUBE SKULL)      (PACK OF 72 SKULL CAKE CASES)   \n",
            "1     (PACK OF 72 SKULL CAKE CASES)      (12 PENCILS SMALL TUBE SKULL)   \n",
            "4    (ASSORTED BOTTLE TOP  MAGNETS)            (36 DOILIES DOLLY GIRL)   \n",
            "5           (36 DOILIES DOLLY GIRL)     (ASSORTED BOTTLE TOP  MAGNETS)   \n",
            "180  (CHILDRENS CUTLERY DOLLY GIRL)  (CHILDRENS CUTLERY CIRCUS PARADE)   \n",
            "\n",
            "     antecedent support  consequent support   support  confidence  lift  \\\n",
            "0              0.055556            0.055556  0.055556         1.0  18.0   \n",
            "1              0.055556            0.055556  0.055556         1.0  18.0   \n",
            "4              0.055556            0.055556  0.055556         1.0  18.0   \n",
            "5              0.055556            0.055556  0.055556         1.0  18.0   \n",
            "180            0.055556            0.055556  0.055556         1.0  18.0   \n",
            "\n",
            "     leverage  conviction  \n",
            "0    0.052469         inf  \n",
            "1    0.052469         inf  \n",
            "4    0.052469         inf  \n",
            "5    0.052469         inf  \n",
            "180  0.052469         inf  \n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "accelerator": "GPU",
    "gpuClass": "standard"
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
