def main(dist):
  if dist <= 200:
    return dist*0.5
  elif dist <= 400:
    return dist*.45
  else:
    return dist*0.35