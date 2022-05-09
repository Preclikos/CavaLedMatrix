
def parse_config_file(external, channels, bars, size, freq):
  template = open("configs/template", "r")
  internal = open("configs/internal", "r")
  external = open("configs/external", "r")
  config = open("configs/config", "w")

  template_data = template.read()
  template.close()
  source_data = ""
  if(external == True):
    source_data = external.read()
  else:
    source_data = internal.read()
  template_data = template_data.replace("[Input_Replace]", source_data)
  internal.close()
  external.close()

  template_data = template_data.replace("[Channels_Replace]", channels)
  template_data = template_data.replace("[Bars_Replace]", str(bars))
  template_data = template_data.replace("[Size_Replace]", str(size))
  template_data = template_data.replace("[Freq_Replace]", str(freq))
  
  config.write(template_data)
  config.close()
