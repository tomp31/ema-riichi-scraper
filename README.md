# 🀄 EMA Tournament Scraper andRankings Calculator

Save a bunch of tournament pages locally and then scrape them for data.

Then calculate both the MERS and RUKRS rankings.

## 📥 Installation

### 1️⃣ Clone the Repository

```shell
git clone https://github.com/ea-ncu/ema-riichi-scraper
cd ema-riichi-scraper
```

### 2️⃣ Install Dependencies

Ensure you have Python installed (>=3.7). Then install required packages:

```shell
pip install -r requirements.txt
```

### 3️⃣ Setup PostgreSQL Database

Ensure PostgreSQL is running and create a database:

```postgresql
create database riichi;
```

Run the commands found in `postgres/init.sql`

If needed, add a `DBCONN` environment variable or modify the `DBCONN` values stored in the Python files

## 🚀 Usage

### 1️⃣ Download Tournament Pages

Download tournament pages for offline use/scraping:

```shell
python download_tournaments.py 285 363
```

There is some additional code to fix some files so that the date can be parsed correctly.

### 2️⃣ Parse and Store Tournament Data

To extract data from downloaded pages and store it in PostgreSQL:

```shell
python save_tournaments.py 285 363
```

### 3️⃣ Run scripts to calculate rankings

Running the following scripts sets the corresponding columns on the players table in the database.

```shell
python calculate_current_mers.py
python calculate_current_rukrs.py
```
