CREATE TABLE buy (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT,
    symbols TEXT NOT NULL,
    shares INTEGER NOT NULL,
    buy_price INTEGER NOT NULL,
    transaction_time TEXT NOT NULL
);

CREATE TABLE sell (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT,
    symbols TEXT NOT NULL,
    shares INTEGER,
    shares_left INTEGER NOT NULL,
    sell_price INTEGER NOT NULL,
    trasaction_time TEXT NOT NULL
);
-- selecting available cash from the table users
SELECT cash FROM users WHERE username ="username";
--upadating the cash after purchase
UPDATE users SET cash = ""

-- available cash before - share * price

-- finding shares for each stocks
db.execute("SELECT UNIQUE symbols FROM buy WHERE user_id = ?", username[0]["username"])
--cash, symbols, shares total
SELECT symbols, cash, shares

--selecting and adding shares from the common symbols
SELECT symbols, SUM(shares) FROM buy WHERE user_id = "aarav497" GROUP BY symbols;

--https://www.edx.org/professional-certificate/linuxfoundationx-open-source-software-development-linux-and-git?index=product&queryID=24d0d81c4b958f4c0f1a320c38c1d000&position=8&linked_from=autocomplete&c=autocomplete


--username mismatching in sql db solved when entering the stock
---finding usernmae using defined function
--correcting the for loop, misunderstandings
--indexing completed used jinja instead of python
-- --       {% for items in portfolio%}
--             <tr>
--                 <td>{{ items.symbols }}</td>
--                 <td>{{ items.total_shares }}</td>
--                 {% for data in data_list%}
--                     {% if data.symbol == items.symbols %}
--                         <td>{{ data.price }}</td>
--                         <td>{{ items.total_shares * data.price }}</td>
--                     {% endif %}
--                 {% endfor %}

--             </tr>
--         {% endfor %}
-- idea came from my mind proud of that
-- CREATE TABLE shares(
--     user_id TEXT,
--     symbols TEXT NOT NULL,
--     shares INTEGER
-- )
SELECT buy.shares+sell.shares AS total_shares FROM buy Join sell ON buy.user_id = sell.user_id;


-- ALTER TABLE sell MODIFY COLUMN shares INTEGER DEFAULT 0;

CREATE TABLE sell (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT,
    symbols TEXT NOT NULL,
    shares INTEGER DEFAULT 0 NOT NULL,
    sell_price INTEGER NOT NULL,
    trasaction_time TEXT NOT NULL
);
-UPDATE sell SET shares = u

SELECT SUM(shares) AS sumsShares FROM sell where user_id = "kk" AND symbols = "NFLX";

--finding the availbale share challenge solved by finding the sum of
-- columns of seperately once in buy and then in sell
-- then subtracting both

----in index sum of shares to solve with the remaining shares
SELECT buy.symbols, buy.shares + sell.shares From buy JOIN sell ON buy.user_id = sell.user_id GROUP BY buy.symbols;

SELECT symbols, SUM(shares) from sell where user_id = "kk" group by symbols;
SELECT symbols, SUM(shares) from buy where user_id = "kk" group by symbols

---changing everythhing, deleting buy and sell tables and create a transaction table of combined
-- modifying everthing according to new table
--