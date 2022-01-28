def unicode_test ( value ):
    import unicodedata
    name = unicodedata . name ( value ) 
    value2 = unicodedata . lookup ( name )
    print ( 'value=" %s ", name=" %s ", value2=" %s "' % ( value , name , value2 )) 

unicode_test('A')
value=" A ", name=" LATIN CAPITAL LETTER A ", value2=" A "


unicodedata.lookup ('LATIN SMALL LETTER E WITH ACUTE') 

snowman = ' \u2603 ' 

snowman