# Robodzejnieks

Šis ir Discord bots, kas izmanto Edvarta Veidenbauma dzeju. Bots spēj parādīt nejaušu dzejoli un arī uzģenerēt jaunu dzejoli, izmantojot esošās rindas no dzejoļiem.

## Kā tas strādā

Lai palaistu botu:
1. Saglabā savu Discord bota `token` failā `bot_key.txt`.
2. Saglabā visus dzejoļus `.txt` formātā mapē `poems/`.
3. Palaid `main.py`.

## Komandas

**!dzeja**  
Parāda nejauši izvēlētu dzejoli no mapes `poems/`. Ir iespējams pievienot vēl.

**!ģenerēt**  
Ģenerē jaunu dzejoli, izmantojot rindas no esošajiem dzejoļiem (4 rindas nejaušā kārtībā).

**!dzīvs**  
Sūta ziņu “Esmu dzīvs!”, lai pārliecinātos, ka bots darbojas. Šī komanda palīdz testēt, vai botam ir spēja lasīt un sūtīt ziņas/

## Piezīmes

- Dzejoļiem jābūt `.txt` failos, katrā pa vienam dzejolim.
