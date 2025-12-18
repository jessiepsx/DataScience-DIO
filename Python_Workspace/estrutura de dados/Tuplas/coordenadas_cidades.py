#localizacao = ((40.71, -74.01), (47.20, 90.03),(18.99, -76.02) )

#nova_york = (40.71, -74.01)
#alemanha = (47.20, 90.03)
#argentina = (18.99, -76.02)

#cidades_a_visitar = [nova_york, alemanha, argentina]
#print(cidades_a_visitar [1])


cidades_a_visitar = [('Nova York', 40.71, -74.01),  ('Tóquio',47.20, 90.03), ('Paris', 18.99, -76.02)]

print(cidades_a_visitar[1][2])

for nome_cidade, lat, long in cidades_a_visitar:
    print(f'A cidade {nome_cidade} esta em Lat:{lat}, Long: {long}')