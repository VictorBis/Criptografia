import prime_generator as gen

primes = [3, 5, 7, 11,
          7636753809170479014279798314827088025065336332353517219804499910251032263408265688451518206781272437001625717228465749506582632334873719180181007941145427,
          9876726757293014109322765731397582603056107233851215617938670499662811324799183084036870012358188134578519755597927711228130030007929996604299613694468793,
          9838904645695721399467507393637950834772530843079566176626772344224146023275504290547965580877752204878078969621050913955161578722652608345125565299893441]

not_primes = [4, 6, 8, 22,
              13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096,
              139008452377144732764939786789661303114218850808529137991604824430036072629766435941001769154109609521811665540548899435521,
              86361685550944446253863518628003995711160003644362813850237034701685918031624270579715075034722882265605472939461496635969950989468319466936530037770580747746862471103668212890625]

def test_very_large_number():
    first, snd, thd= str(gen.big_int(100)), str(gen.big_int()), str(gen.big_int(99))
    assert len(first) == 100
    assert len(snd) >= 100 and len(snd) <= 150
    assert len(thd) >= 100 and len(thd) <= 150

def test_miller_rabin():
    for p in primes:
        assert gen.miller_rabin(p)
    for np in not_primes:
        assert not(gen.miller_rabin(np))
"""
def test_wilson():
    for p in primes:
        assert gen.wilson(p)
    for np in not_primes:
        assert not(gen.wilson(np))
"""
