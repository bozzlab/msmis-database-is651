# Database IS651

## Prerequisites

1. Install Python libraries

    ```sh
    pipenv install
    ```

1. Set up Database Credentials in `.env`

    ```sh
    DB_HOST=
    DB_NAME=
    DB_PORT=
    DB_USER=
    DB_PASS=
    ```

1. Run the initial SQL script (optional) This script is located at: 

    `sql_scripts/create.sql`

1. Generate models from the database (optional)

    ```sh
    sqlacodegen postgresql://DB_USER:DB_PASS@DB_HOST:DB_PORT/DB_NAME --outfile models/models.py
    ```

## Development

1. Run the latest migration

    ```sh
    alembic upgrade head
    ```

1. Create a new migration

    ```sh
    alembic revision --autogenerate -m "message"
    ```

1. Populate Data

    ```sh
    python main.py 
    ```

1. Format Code

    ```sh
    ruff format .
    ```


## Populate data 

Write your custom population script in `main.py`

Sample Logs:


<details>

```sh
... [Factory Session] Injecting session into BaseFactory ...
Created user: 6 - robert.jones0@msmis.com
Created user: 7 - kathleen.mueller1@hotmail.com
Created user: 8 - jennifer.alvarez2@msmis.com
Created user: 9 - vicki.rodriguez3@hotmail.com
Created user: 10 - derrick.gonzalez4@hotmail.com
Created expense category for user 6: 1 - Food
Created expense category for user 6: 2 - Transport
Created expense category for user 6: 3 - Shopping
Created income category for user 6: 1 - Salary
Created income category for user 6: 2 - Bonus
Created income category for user 6: 3 - Freelance
Created expense category for user 7: 4 - Bills
Created expense category for user 7: 5 - Food
Created expense category for user 7: 6 - Transport
Created income category for user 7: 4 - Investment
Created income category for user 7: 5 - Salary
Created income category for user 7: 6 - Bonus
Created expense category for user 8: 7 - Shopping
Created expense category for user 8: 8 - Bills
Created expense category for user 8: 9 - Food
Created income category for user 8: 7 - Freelance
Created income category for user 8: 8 - Investment
Created income category for user 8: 9 - Salary
Created expense category for user 9: 10 - Transport
Created expense category for user 9: 11 - Shopping
Created expense category for user 9: 12 - Bills
Created income category for user 9: 10 - Bonus
Created income category for user 9: 11 - Freelance
Created income category for user 9: 12 - Investment
Created expense category for user 10: 13 - Food
Created expense category for user 10: 14 - Transport
Created expense category for user 10: 15 - Shopping
Created income category for user 10: 13 - Salary
Created income category for user 10: 14 - Bonus
Created income category for user 10: 15 - Freelance
Created expense transaction for user 6: 1 - incentivize vertical bandwidth - 513.87
Created expense transaction for user 6: 2 - optimize impactful communities - 830.98
Created expense transaction for user 6: 3 - integrate rich models - 144.92
Created expense transaction for user 6: 4 - unleash real-time supply-chains - 244.24
Created expense transaction for user 6: 5 - e-enable visionary partnerships - 948.89
Created expense transaction for user 6: 6 - empower back-end info-mediaries - 649.22
Created expense transaction for user 6: 7 - embrace B2B metrics - 112.62
Created expense transaction for user 6: 8 - e-enable visionary channels - 179.39
Created expense transaction for user 6: 9 - e-enable integrated functionalities - 874.08
Created expense transaction for user 6: 10 - reinvent frictionless communities - 349.50
Created income transaction for user 6: 1 - integrate efficient portals - 5356.51
Created income transaction for user 6: 2 - visualize B2B schemas - 5660.62
Created income transaction for user 6: 3 - deploy intuitive experiences - 2894.50
Created income transaction for user 6: 4 - redefine global supply-chains - 2728.22
Created income transaction for user 6: 5 - monetize B2B markets - 6535.81
Created income transaction for user 6: 6 - redefine out-of-the-box bandwidth - 3984.34
Created income transaction for user 6: 7 - disintermediate frictionless synergies - 8020.29
Created income transaction for user 6: 8 - brand seamless initiatives - 2425.75
Created income transaction for user 6: 9 - synthesize B2C solutions - 2124.18
Created income transaction for user 6: 10 - cultivate intuitive action-items - 1201.71
Created expense transaction for user 7: 11 - seize customized e-commerce - 838.33
Created expense transaction for user 7: 12 - harness collaborative e-services - 929.88
Created expense transaction for user 7: 13 - scale plug-and-play functionalities - 550.30
Created expense transaction for user 7: 14 - monetize plug-and-play partnerships - 268.59
Created expense transaction for user 7: 15 - seize granular supply-chains - 891.80
Created expense transaction for user 7: 16 - utilize global solutions - 427.45
Created expense transaction for user 7: 17 - transform efficient methodologies - 130.81
Created expense transaction for user 7: 18 - strategize scalable experiences - 507.49
Created expense transaction for user 7: 19 - grow dynamic schemas - 733.06
Created expense transaction for user 7: 20 - generate bricks-and-clicks partnerships - 178.93
Created income transaction for user 7: 11 - enable transparent deliverables - 5898.98
Created income transaction for user 7: 12 - disintermediate revolutionary models - 5098.67
Created income transaction for user 7: 13 - reinvent value-added convergence - 2405.09
Created income transaction for user 7: 14 - strategize user-centric solutions - 3320.14
Created income transaction for user 7: 15 - grow killer metrics - 1859.43
Created income transaction for user 7: 16 - brand ubiquitous supply-chains - 3395.24
Created income transaction for user 7: 17 - empower innovative mindshare - 3554.49
Created income transaction for user 7: 18 - benchmark back-end deliverables - 3489.81
Created income transaction for user 7: 19 - incubate bleeding-edge deliverables - 8701.53
Created income transaction for user 7: 20 - syndicate viral technologies - 1700.33
Created expense transaction for user 8: 21 - engineer vertical partnerships - 270.13
Created expense transaction for user 8: 22 - e-enable seamless partnerships - 487.44
Created expense transaction for user 8: 23 - leverage bleeding-edge synergies - 622.80
Created expense transaction for user 8: 24 - repurpose clicks-and-mortar schemas - 668.06
Created expense transaction for user 8: 25 - enable compelling paradigms - 785.48
Created expense transaction for user 8: 26 - implement bleeding-edge info-mediaries - 832.52
Created expense transaction for user 8: 27 - evolve 24/7 metrics - 370.10
Created expense transaction for user 8: 28 - cultivate leading-edge e-services - 458.86
Created expense transaction for user 8: 29 - enable 24/7 mindshare - 697.64
Created expense transaction for user 8: 30 - enhance bleeding-edge methodologies - 844.74
Created income transaction for user 8: 21 - evolve best-of-breed metrics - 3201.06
Created income transaction for user 8: 22 - envisioneer global markets - 5400.10
Created income transaction for user 8: 23 - deploy cross-platform e-commerce - 6729.74
Created income transaction for user 8: 24 - syndicate visionary convergence - 9456.55
Created income transaction for user 8: 25 - streamline seamless action-items - 5461.61
Created income transaction for user 8: 26 - drive back-end methodologies - 2418.88
Created income transaction for user 8: 27 - maximize bricks-and-clicks mindshare - 6715.14
Created income transaction for user 8: 28 - engage impactful ROI - 5198.97
Created income transaction for user 8: 29 - unleash open-source deliverables - 6636.32
Created income transaction for user 8: 30 - brand visionary communities - 4497.50
Created expense transaction for user 9: 31 - engage compelling channels - 799.85
Created expense transaction for user 9: 32 - revolutionize cutting-edge functionalities - 383.81
Created expense transaction for user 9: 33 - strategize cross-platform action-items - 891.53
Created expense transaction for user 9: 34 - evolve killer markets - 643.59
Created expense transaction for user 9: 35 - monetize compelling portals - 627.48
Created expense transaction for user 9: 36 - engage interactive vortals - 691.86
Created expense transaction for user 9: 37 - strategize extensible systems - 674.12
Created expense transaction for user 9: 38 - productize vertical synergies - 938.45
Created expense transaction for user 9: 39 - repurpose revolutionary niches - 961.42
Created expense transaction for user 9: 40 - synthesize visionary paradigms - 986.25
Created income transaction for user 9: 31 - incentivize out-of-the-box channels - 5136.53
Created income transaction for user 9: 32 - streamline granular action-items - 1680.65
Created income transaction for user 9: 33 - e-enable robust action-items - 2997.53
Created income transaction for user 9: 34 - synergize integrated schemas - 4888.03
Created income transaction for user 9: 35 - evolve frictionless metrics - 4716.09
Created income transaction for user 9: 36 - transition one-to-one niches - 6802.17
Created income transaction for user 9: 37 - unleash compelling architectures - 5169.92
Created income transaction for user 9: 38 - optimize strategic interfaces - 7216.59
Created income transaction for user 9: 39 - empower bleeding-edge models - 8325.87
Created income transaction for user 9: 40 - repurpose scalable web services - 8565.90
Created expense transaction for user 10: 41 - revolutionize magnetic experiences - 309.84
Created expense transaction for user 10: 42 - e-enable ubiquitous infrastructures - 543.56
Created expense transaction for user 10: 43 - facilitate real-time networks - 705.85
Created expense transaction for user 10: 44 - expedite user-centric relationships - 546.48
Created expense transaction for user 10: 45 - incubate extensible channels - 392.83
Created expense transaction for user 10: 46 - drive intuitive e-business - 962.78
Created expense transaction for user 10: 47 - productize 24/365 eyeballs - 286.27
Created expense transaction for user 10: 48 - re-intermediate magnetic supply-chains - 245.20
Created expense transaction for user 10: 49 - iterate sticky e-commerce - 992.19
Created expense transaction for user 10: 50 - generate value-added e-business - 300.57
Created income transaction for user 10: 41 - cultivate back-end systems - 2141.82
Created income transaction for user 10: 42 - seize next-generation e-tailers - 1327.93
Created income transaction for user 10: 43 - embrace cross-platform web services - 5466.07
Created income transaction for user 10: 44 - expedite value-added info-mediaries - 2692.25
Created income transaction for user 10: 45 - matrix ubiquitous portals - 4792.78
Created income transaction for user 10: 46 - evolve dynamic communities - 2961.35
Created income transaction for user 10: 47 - cultivate distributed e-markets - 5307.29
Created income transaction for user 10: 48 - matrix cross-media info-mediaries - 9369.76
Created income transaction for user 10: 49 - engineer killer technologies - 7057.77
Created income transaction for user 10: 50 - embrace value-added interfaces - 7448.77
```


</details>


Sample Output at `expense_transactions`

<details>

```md
| id | user_id | transaction_datetime       | name                                       | amount | category_id | currency_id | exclude_from_goal | note                                                       | payment_method_id | last_modified_at           | created_at                 |
| -- | ------- | -------------------------- | ------------------------------------------ | ------ | ----------- | ----------- | ----------------- | ---------------------------------------------------------- | ----------------- | -------------------------- | -------------------------- |
| 7  | 6       | 2025-11-05 04:16:45.300523 | embrace B2B metrics                        | 112.62 | 22          | 22          | false             | Order like adult mission go remember accept.               | 7                 | 2025-11-05 09:32:05.565087 | 2025-11-05 09:32:05.565087 |
| 8  | 6       | 2025-11-04 06:59:40.747365 | e-enable visionary channels                | 179.39 | 23          | 23          | false             | Common item southern choose medical ability scene.         | 8                 | 2025-11-05 09:32:05.578287 | 2025-11-05 09:32:05.578287 |
| 9  | 6       | 2025-11-04 09:13:13.211218 | e-enable integrated functionalities        | 874.08 | 24          | 24          | false             | Fear goal question whole Republican population pattern.    | 9                 | 2025-11-05 09:32:05.590371 | 2025-11-05 09:32:05.590371 |
| 10 | 6       | 2025-11-03 08:45:29.673978 | reinvent frictionless communities          | 349.50 | 25          | 25          | false             | Position election standard process.                        | 10                | 2025-11-05 09:32:05.602225 | 2025-11-05 09:32:05.602225 |
| 11 | 7       | 2025-11-02 06:52:34.372706 | seize customized e-commerce                | 838.33 | 26          | 36          | false             | You investment skin above result last.                     | 11                | 2025-11-05 09:32:05.746545 | 2025-11-05 09:32:05.746545 |
| 12 | 7       | 2025-11-01 14:27:50.830855 | harness collaborative e-services           | 929.88 | 27          | 37          | false             | Expect few attack you believe plan.                        | 12                | 2025-11-05 09:32:05.758019 | 2025-11-05 09:32:05.758019 |
| 13 | 7       | 2025-11-04 23:38:07.666797 | scale plug-and-play functionalities        | 550.30 | 28          | 38          | false             | That they campaign reason moment buy.                      | 13                | 2025-11-05 09:32:05.769867 | 2025-11-05 09:32:05.769867 |
| 14 | 7       | 2025-11-01 15:02:33.277946 | monetize plug-and-play partnerships        | 268.59 | 29          | 39          | false             | Entire major material.                                     | 14                | 2025-11-05 09:32:05.782401 | 2025-11-05 09:32:05.782401 |
| 15 | 7       | 2025-11-02 05:10:59.858328 | seize granular supply-chains               | 891.80 | 30          | 40          | false             | Great special bank cup new.                                | 15                | 2025-11-05 09:32:05.794937 | 2025-11-05 09:32:05.794937 |
| 16 | 7       | 2025-11-04 14:17:01.628752 | utilize global solutions                   | 427.45 | 31          | 41          | false             | Hand ground conference range accept force family.          | 16                | 2025-11-05 09:32:05.807722 | 2025-11-05 09:32:05.807722 |
| 17 | 7       | 2025-11-03 12:31:53.59461  | transform efficient methodologies          | 130.81 | 32          | 42          | false             | Laugh message guy under.                                   | 17                | 2025-11-05 09:32:05.821091 | 2025-11-05 09:32:05.821091 |
| 18 | 7       | 2025-11-02 18:37:37.07889  | strategize scalable experiences            | 507.49 | 33          | 43          | false             | Perhaps fine difference employee democratic resource plan. | 18                | 2025-11-05 09:32:05.833019 | 2025-11-05 09:32:05.833019 |
| 19 | 7       | 2025-11-02 13:01:44.466738 | grow dynamic schemas                       | 733.06 | 34          | 44          | false             | Cause another world picture sea practice threat.           | 19                | 2025-11-05 09:32:05.844307 | 2025-11-05 09:32:05.844307 |
| 20 | 7       | 2025-11-02 11:36:30.912562 | generate bricks-and-clicks partnerships    | 178.93 | 35          | 45          | false             | Picture commercial future both.                            | 20                | 2025-11-05 09:32:05.856841 | 2025-11-05 09:32:05.856841 |
| 21 | 8       | 2025-11-02 08:56:26.621501 | engineer vertical partnerships             | 270.13 | 36          | 56          | false             | May get organization care window.                          | 21                | 2025-11-05 09:32:06.001419 | 2025-11-05 09:32:06.001419 |
| 22 | 8       | 2025-11-02 07:33:52.201315 | e-enable seamless partnerships             | 487.44 | 37          | 57          | false             | Blue certain could be total civil.                         | 22                | 2025-11-05 09:32:06.020155 | 2025-11-05 09:32:06.020155 |
| 23 | 8       | 2025-11-01 03:16:52.872072 | leverage bleeding-edge synergies           | 622.80 | 38          | 58          | false             | Only special bank they teach help long.                    | 23                | 2025-11-05 09:32:06.040119 | 2025-11-05 09:32:06.040119 |
| 24 | 8       | 2025-11-04 00:20:04.020775 | repurpose clicks-and-mortar schemas        | 668.06 | 39          | 59          | false             | Lose toward case kitchen Democrat.                         | 24                | 2025-11-05 09:32:06.054966 | 2025-11-05 09:32:06.054966 |
| 25 | 8       | 2025-11-03 07:01:45.232627 | enable compelling paradigms                | 785.48 | 40          | 60          | false             | Opportunity reason simply seat.                            | 25                | 2025-11-05 09:32:06.069614 | 2025-11-05 09:32:06.069614 |
| 26 | 8       | 2025-11-04 22:18:36.838481 | implement bleeding-edge info-mediaries     | 832.52 | 41          | 61          | false             | Training else pattern hit.                                 | 26                | 2025-11-05 09:32:06.081173 | 2025-11-05 09:32:06.081173 |
| 27 | 8       | 2025-11-03 15:45:45.853265 | evolve 24/7 metrics                        | 370.10 | 42          | 62          | false             | Energy present move save they.                             | 27                | 2025-11-05 09:32:06.093432 | 2025-11-05 09:32:06.093432 |
| 28 | 8       | 2025-11-04 20:55:21.969639 | cultivate leading-edge e-services          | 458.86 | 43          | 63          | false             | According rise hit.                                        | 28                | 2025-11-05 09:32:06.10492  | 2025-11-05 09:32:06.10492  |
| 29 | 8       | 2025-11-04 07:53:03.881608 | enable 24/7 mindshare                      | 697.64 | 44          | 64          | false             | Carry never better scene expect series.                    | 29                | 2025-11-05 09:32:06.116247 | 2025-11-05 09:32:06.116247 |
| 30 | 8       | 2025-11-05 00:57:32.503841 | enhance bleeding-edge methodologies        | 844.74 | 45          | 65          | false             | Week list fund music compare.                              | 30                | 2025-11-05 09:32:06.128205 | 2025-11-05 09:32:06.128205 |
| 31 | 9       | 2025-11-03 17:30:18.271127 | engage compelling channels                 | 799.85 | 46          | 76          | false             | Others thought how determine provide under deep play.      | 31                | 2025-11-05 09:32:06.262945 | 2025-11-05 09:32:06.262945 |
| 32 | 9       | 2025-11-02 20:09:01.879977 | revolutionize cutting-edge functionalities | 383.81 | 47          | 77          | false             | Color environmental evening cost.                          | 32                | 2025-11-05 09:32:06.274464 | 2025-11-05 09:32:06.274464 |
| 33 | 9       | 2025-11-05 05:21:04.79037  | strategize cross-platform action-items     | 891.53 | 48          | 78          | false             | Smile consumer piece well be.                              | 33                | 2025-11-05 09:32:06.286786 | 2025-11-05 09:32:06.286786 |
| 34 | 9       | 2025-11-02 03:59:55.0262   | evolve killer markets                      | 643.59 | 49          | 79          | false             | Fill memory page affect perform where.                     | 34                | 2025-11-05 09:32:06.297679 | 2025-11-05 09:32:06.297679 |
| 35 | 9       | 2025-11-02 16:26:15.963997 | monetize compelling portals                | 627.48 | 50          | 80          | false             | Surface character word picture citizen song watch.         | 35                | 2025-11-05 09:32:06.310517 | 2025-11-05 09:32:06.310517 |
| 36 | 9       | 2025-11-04 13:55:46.66708  | engage interactive vortals                 | 691.86 | 51          | 81          | false             | Difference wide movement yourself write owner.             | 36                | 2025-11-05 09:32:06.322662 | 2025-11-05 09:32:06.322662 |
| 37 | 9       | 2025-11-02 10:01:43.317094 | strategize extensible systems              | 674.12 | 52          | 82          | false             | Window new tonight.                                        | 37                | 2025-11-05 09:32:06.333794 | 2025-11-05 09:32:06.333794 |
| 38 | 9       | 2025-11-01 02:23:23.446202 | productize vertical synergies              | 938.45 | 53          | 83          | false             | Worker owner page beat race pull.                          | 38                | 2025-11-05 09:32:06.346312 | 2025-11-05 09:32:06.346312 |
| 39 | 9       | 2025-11-04 00:54:29.274769 | repurpose revolutionary niches             | 961.42 | 54          | 84          | false             | Side student gas early girl car follow.                    | 39                | 2025-11-05 09:32:06.358054 | 2025-11-05 09:32:06.358054 |
| 40 | 9       | 2025-11-01 01:54:41.032322 | synthesize visionary paradigms             | 986.25 | 55          | 85          | false             | Herself its especially memory drive director conference.   | 40                | 2025-11-05 09:32:06.37115  | 2025-11-05 09:32:06.37115  |
| 41 | 10      | 2025-11-05 03:35:41.017549 | revolutionize magnetic experiences         | 309.84 | 56          | 96          | false             | Each sell shoulder.                                        | 41                | 2025-11-05 09:32:06.512811 | 2025-11-05 09:32:06.512811 |
| 42 | 10      | 2025-11-04 16:40:30.821046 | e-enable ubiquitous infrastructures        | 543.56 | 57          | 97          | false             | Quality vote usually.                                      | 42                | 2025-11-05 09:32:06.52554  | 2025-11-05 09:32:06.52554  |
| 43 | 10      | 2025-11-01 15:14:08.551819 | facilitate real-time networks              | 705.85 | 58          | 98          | false             | Firm live gas would.                                       | 43                | 2025-11-05 09:32:06.537487 | 2025-11-05 09:32:06.537487 |
| 44 | 10      | 2025-11-02 13:58:30.034897 | expedite user-centric relationships        | 546.48 | 59          | 99          | false             | Draw nature necessary remember decision recently.          | 44                | 2025-11-05 09:32:06.54979  | 2025-11-05 09:32:06.54979  |
| 45 | 10      | 2025-11-03 16:39:49.848976 | incubate extensible channels               | 392.83 | 60          | 100         | false             | Street TV trial I.                                         | 45                | 2025-11-05 09:32:06.56251  | 2025-11-05 09:32:06.56251  |
| 46 | 10      | 2025-11-02 22:02:53.881527 | drive intuitive e-business                 | 962.78 | 61          | 101         | false             | Benefit where decade coach language table.                 | 46                | 2025-11-05 09:32:06.574996 | 2025-11-05 09:32:06.574996 |
| 47 | 10      | 2025-11-02 07:40:29.605139 | productize 24/365 eyeballs                 | 286.27 | 62          | 102         | false             | Could young style like.                                    | 47                | 2025-11-05 09:32:06.586397 | 2025-11-05 09:32:06.586397 |
| 48 | 10      | 2025-11-01 01:55:10.907266 | re-intermediate magnetic supply-chains     | 245.20 | 63          | 103         | false             | Quality traditional young your.                            | 48                | 2025-11-05 09:32:06.599113 | 2025-11-05 09:32:06.599113 |
| 49 | 10      | 2025-11-04 16:31:53.017491 | iterate sticky e-commerce                  | 992.19 | 64          | 104         | false             | Quality program market well blue since buy image.          | 49                | 2025-11-05 09:32:06.611545 | 2025-11-05 09:32:06.611545 |
| 50 | 10      | 2025-11-01 18:31:56.626906 | generate value-added e-business            | 300.57 | 65          | 105         | false             | One question like beyond city onto maybe.                  | 50                | 2025-11-05 09:32:06.623093 | 2025-11-05 09:32:06.623093 |
```

</detail>
