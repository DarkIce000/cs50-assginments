-- Keep a log of any SQL queries you execute as you solve the mystery.
--checking for the crime scene report for the first step
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' and year = '2021' and month = '7' and day = '28';
-- | 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

--from crime scene table i got to know that t%¹here were three witnesses that were interviewed, hence cheking for transcript
SELECT id, name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

-- | 162 | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | 163 | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |




--fin po po poding the atm location from which the thief has transacted money before commiting the crime
--by eugene transcript thief transacted by a atm that is located in leggett  street, on morning of crime
SELECT account_number, amount, transaction_type
FROM atm_transactions
WHERE atm_location = 'Leggett Street'
    AND year = '2021'
    AND month = '7'
    AND day = '28';
-- +----------------+--------+------------------+
-- | account_number | amount | transaction_type |
-- +----------------+--------+------------------+
-- | 28500762       | 48     | withdraw         |
-- | 28296815       | 20     | withdraw         |
-- | 76054385       | 60     | withdraw         |
-- | 49610011       | 50     | withdraw         |
-- | 16153065       | 80     | withdraw         |
-- | 86363979       | 10     | deposit          |
-- | 25506511       | 20     | withdraw         |
-- | 81061156       | 30     | withdraw         |
-- | 26013199       | 35     | withdraw         |
-- +----------------+--------+------------------+

--now finding the person id  from the account number detail

---person id from atm
SELECT person_id
FROM bank_accounts
WHERE account_number
IN(SELECT account_number
    FROM atm_transactions
    WHERE atm_location = 'Leggett Street'
        AND year = '2021'
        AND month = '7'
        AND day = '28');
-- --+-----------+---------------+
-- | person_id | creation_year |
-- +-----------+---------------+
-- | 686048    | 2010          |
-- | 948985    | 2010          |
-- | 514354    | 2012          |
-- | 458378    | 2012          |
-- | 395717    | 2014          |
-- | 396669    | 2014          |
-- | 467400    | 2014          |
-- | 449774    | 2015          |
-- | 438727    | 2018          |
-- +-----------+---------------+

-- person id from first flight that is on 29 july

SELECT passport_number
FROM passengers
WHERE flight_id = 36;
  ---now selecting person id
  SELECT id
  FROM people
  WHERE passport_number
  IN(SELECT passport_number
    FROM passengers
    WHERE flight_id = 36);


-----------------------------------------------------
--now selecting person id which has license plate in bakery security logs
SELECT id
FROM people
WHERE license_plate
IN (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute between 15 to 25);


-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------

-- now intersecting those three person id
SELECT id
FROM people
WHERE license_plate
IN (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute between 15 AND 25);

INTERSECT
SELECT person_id
FROM bank_accounts
WHERE account_number
IN(SELECT account_number
    FROM atm_transactions
    WHERE atm_location = 'Leggett Street'
        AND year = '2021'
        AND month = '7'
        AND day = '28')

INTERSECT

SELECT id FROM people WHERE passport_number IN
(SELECT passport_number FROM flights
JOIN passengers ON flights.id = passengers.flight_id
WHERE flight_id = 36
    AND year = 2021
    AND month = 7
    AND day = 29);

-- +--------+
-- |  name  |
-- +--------+
-- | Taylor |
-- | Luca   |
-- | Bruce  |

SELECT passport_number FROM flights
JOIN passengers ON flights.id = passengers.flight_id
WHERE flight_id = 36
    AND year = 2021
    AND month = 7
    AND day = 29;

SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM flights
JOIN passengers ON flights.id = passengers.flight_id
WHERE flight_id = 36
    AND year = 2021
    AND month = 7
    AND day = 29);



--------------------------------------
-- FROM here on that is my last try and got the answer
-- my thought process is finding the common person that link to all of the conditions
-- such as passengers from first flight from 19 july, person id from atm transaction, license plate from bakery, and phone call made by theif



----------------------------------------------
SELECT id FROM airports WHERE city = 'Fiftyville';

------------------
SELECT id
FROM people
WHERE license_plate
IN (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute between 15 AND 25
)

INTERSECT

SELECT person_id
FROM bank_accounts
WHERE account_number
IN(SELECT account_number
    FROM atm_transactions
    WHERE atm_location = 'Leggett Street'
        AND year = '2021'
        AND month = '7'
        AND day = '28')

INTERSECT

SELECT id
FROM people
WHERE passport_number
IN(SELECT passport_number
    FROM flights
    JOIN passengers ON flights.id = passengers.flight_id
    WHERE flight_id = 36
    AND origin_airport_id = 8
    AND year = 2021
    AND month = 7
    AND day = 29)

INTERSECT

SELECT id
FROM people
WHERE phone_number
IN (
    SELECT caller
    FROM phone_calls
    WHERE
    year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
);



-------------------
--finding the accomplice
-----------------

SELECT name, phone_number
FROM people
WHERE phone_number
= (
    SELECT receiver
    FROM phone_calls
    WHERE
    year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
    AND caller = '(367) 555-5533'
);

---| Bruce   | (367) 555-5533 |
--------------------------------
---| Robin | (375) 555-8161
---------------------------------------------------
SELECT destination_airport_id
    FROM flights
    JOIN passengers ON flights.id = passengers.flight_id
    WHERE flight_id = 36
    AND origin_airport_id = 8
    AND year = 2021
    AND month = 7
    AND day = 29
 -- from this i get id of the city thief escaped to
 --destination_airport_id = 4;
 -------------------------------------------
 --finding city
 SELECT city, full_name
 FROM airports
 WHERE id = 4;
