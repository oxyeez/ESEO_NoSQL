# 1.0 Load artists.json

``` bash
 mongoimport --db cours --collection artists --file ~/Downloads/artists.json –jsonArray
 ```

# 1.1 Return first_name and birth_date to all artists born in 1964

```bash
cours> db.artists.find({"birth_date":{$eq:"1964"}}, {first_name:1, birth_date:1})
[
  { _id: 'artist:12', first_name: 'Nicolas', birth_date: '1964' },
  { _id: 'artist:14', first_name: 'Johnny', birth_date: '1964' },
  { _id: 'artist:23', first_name: 'Russell', birth_date: '1964' },
  { _id: 'artist:43', first_name: 'Mat', birth_date: '1964' },
  { _id: 'artist:62', first_name: 'Keanu', birth_date: '1964' },
  { _id: 'artist:125', first_name: 'Annabella', birth_date: '1964' },
  { _id: 'artist:144', first_name: 'Tom', birth_date: '1964' },
  { _id: 'artist:169', first_name: 'Bridget', birth_date: '1964' },
  { _id: 'artist:177', first_name: 'Russel', birth_date: '1964' }
]
```

# 1.2 Return all arstists born after 1980 or with their first name begin by ‘Chri’

``` bash
cours> db.artists.find({$or:[{"birth_date":{$gt:"1980"}}, {"first_name":/^Chri/}]}, {first_name:1, birth_date:1})
[
  { _id: 'artist:36', first_name: 'Christian', birth_date: '1969' },
  { _id: 'artist:85', first_name: 'Christian', birth_date: '1952' },
  { _id: 'artist:96', first_name: 'Christina', birth_date: '1980' },
  { _id: 'artist:100', first_name: 'Chris', birth_date: '1966' },
  { _id: 'artist:97', first_name: 'Christopher', birth_date: '1943' },
  { _id: 'artist:118', first_name: 'Natalie', birth_date: '1981' },
  { _id: 'artist:172', first_name: 'Haley Joel', birth_date: '1988' },
  { _id: 'artist:256', first_name: 'Christoph', birth_date: '1956' },
  { _id: 'artist:257', first_name: 'Mélanie', birth_date: '1983' },
  { _id: 'artist:266', first_name: 'Christopher', birth_date: '1970' },
  { _id: 'artist:268', first_name: 'Anne', birth_date: '1982' },
  { _id: 'artist:274', first_name: 'Christian', birth_date: '1974' },
  { _id: 'artist:279', first_name: 'Tahar', birth_date: '1981' }
]
```
# 1.3 Return the 6e to the 9e artist by their name desc

```bash
cours> db.artists.find().sort({last_name:1}).skip(5).limit(4)
[
  {
    _id: 'artist:278',
    last_name: 'Audiard',
    first_name: 'Jacques',
    birth_date: '1952'
  },
  {
    _id: 'artist:75',
    last_name: 'Balasko',
    first_name: 'Josiane',
    birth_date: '1950'
  },
  {
    _id: 'artist:147',
    last_name: 'Baldwin',
    first_name: 'Adam',
    birth_date: '1962'
  },
  {
    _id: 'artist:274',
    last_name: 'Bale',
    first_name: 'Christian',
    birth_date: '1974'
  }
]
```

# 1.4 Insert the following artist:
```bash
cours> db.artists.insertOne({"_id": "artist:282", "last_name": "Bergere", "first_name": "Alexandre", "birth_date": "1992"})
{ acknowledged: true, insertedId: 'artist:282' }
```

# 1.5 Modify by « Jonathan » the first_name of the artists with the id artist:266

```bash
cours> db.artists.updateOne({_id:"artist:266"}, {$set:{first_name:"Jonathan"}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

# 1.6 Add « yoga » to the 282 artist’s hobbies

```bash
{
    _id: 'artist:282',
    last_name: 'Bergere',
    first_name: 'Alexandre',
    birth_date: '1992',
    hobies: [ 'yoga' ]
  }
```

# 1.7 Add « golf », « poney » & « photo » to the 280 artist’s hobbies

```bash
cours> db.artists.updateOne({_id:"artist:280"}, {$push:{hobbies:{$each:["golf","poney","photo"]}}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

# 1.8 Remove « poney » and « photo » from 280 artist’s hobbies

```bash
cours> db.artists.updateOne({_id:"artist:280"}, {$pull:{hobbies:{$in:["poney", "photo"]}}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```