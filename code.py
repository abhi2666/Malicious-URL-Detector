{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Detecting Malicious URL With Machine Learning In Python\n",
    "##### Credits Faizann\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# EDA Packages\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random\n",
    "\n",
    "\n",
    "# Machine Learning Packages\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load Url Data \n",
    "urls_data = pd.read_csv(\"urldata.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(urls_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>url</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>diaryofagameaddict.com</td>\n",
       "      <td>bad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>espdesign.com.au</td>\n",
       "      <td>bad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>iamagameaddict.com</td>\n",
       "      <td>bad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>kalantzis.net</td>\n",
       "      <td>bad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>slightlyoffcenter.net</td>\n",
       "      <td>bad</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      url label\n",
       "0  diaryofagameaddict.com   bad\n",
       "1        espdesign.com.au   bad\n",
       "2      iamagameaddict.com   bad\n",
       "3           kalantzis.net   bad\n",
       "4   slightlyoffcenter.net   bad"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "urls_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data Vectorization Using TfidVectorizer\n",
    "#### Create A tokenizer\n",
    " + Split ,Remove Repetitions and \"Com\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def makeTokens(f):\n",
    "    tkns_BySlash = str(f.encode('utf-8')).split('/')\t# make tokens after splitting by slash\n",
    "    total_Tokens = []\n",
    "    for i in tkns_BySlash:\n",
    "        tokens = str(i).split('-')\t# make tokens after splitting by dash\n",
    "        tkns_ByDot = []\n",
    "        for j in range(0,len(tokens)):\n",
    "            temp_Tokens = str(tokens[j]).split('.')\t# make tokens after splitting by dot\n",
    "            tkns_ByDot = tkns_ByDot + temp_Tokens\n",
    "        total_Tokens = total_Tokens + tokens + tkns_ByDot\n",
    "    total_Tokens = list(set(total_Tokens))\t#remove redundant tokens\n",
    "    if 'com' in total_Tokens:\n",
    "        total_Tokens.remove('com')\t#removing .com since it occurs a lot of times and it should not be included in our features\n",
    "    return total_Tokens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Labels\n",
    "y = urls_data[\"label\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Features\n",
    "url_list = urls_data[\"url\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using Default Tokenizer\n",
    "#vectorizer = TfidfVectorizer()\n",
    "\n",
    "# Using Custom Tokenizer\n",
    "vectorizer = TfidfVectorizer(tokenizer=makeTokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store vectors into X variable as Our XFeatures\n",
    "X = vectorizer.fit_transform(url_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Split into training and testing dataset 80/20 ratio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Model Building\n",
    "#using logistic regression\n",
    "logit = LogisticRegression()\t\n",
    "logit.fit(X_train, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy  0.96163771063\n"
     ]
    }
   ],
   "source": [
    "# Accuracy of Our Model\n",
    "print(\"Accuracy \",logit.score(X_test, y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Predicting With Our Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_predict = [\"google.com/search=jcharistech\",\n",
    "\"google.com/search=faizanahmad\",\n",
    "\"pakistanifacebookforever.com/getpassword.php/\", \n",
    "\"www.radsport-voggel.de/wp-admin/includes/log.exe\", \n",
    "\"ahrenhei.without-transfer.ru/nethost.exe \",\n",
    "\"www.itidea.it/centroesteticosothys/img/_notes/gum.exe\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_predict = vectorizer.transform(X_predict)\n",
    "New_predict = logit.predict(X_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['good' 'good' 'good' 'bad' 'bad' 'bad']\n"
     ]
    }
   ],
   "source": [
    "print(New_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# https://db.aa419.org/fakebankslist.php\n",
    "X_predict1 = [\"www.buyfakebillsonlinee.blogspot.com\", \n",
    "\"www.unitedairlineslogistics.com\",\n",
    "\"www.stonehousedelivery.com\",\n",
    "\"www.silkroadmeds-onlinepharmacy.com\" ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['bad' 'bad' 'bad' 'bad']\n"
     ]
    }
   ],
   "source": [
    "X_predict1 = vectorizer.transform(X_predict1)\n",
    "New_predict1 = logit.predict(X_predict1)\n",
    "print(New_predict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using Default Tokenizer\n",
    "vectorizer = TfidfVectorizer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store vectors into X variable as Our XFeatures\n",
    "X = vectorizer.fit_transform(url_list)\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Model Building\n",
    "\n",
    "logit = LogisticRegression()\t#using logistic regression\n",
    "logit.fit(X_train, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy  0.964622501278\n"
     ]
    }
   ],
   "source": [
    "# Accuracy of Our Model with our Custom Token\n",
    "print(\"Accuracy \",logit.score(X_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Thanks For Watching\n",
    "#J-Secur1ty\n",
    "#Jesus Saves @ JCharisTech"
   ]
  }
 ],
 "metadata": {
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}