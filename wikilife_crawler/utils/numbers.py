# coding=utf-8

class Numbers(object):
    
    @classmethod
    def parse_int(cls, str_value):
        """
        returns int value
        """
        
        str_value = str_value.replace(".", "")
        str_value = str_value.replace(",", "")
        
        return int(str_value)
    
    @classmethod
    def parse_float(cls, str_value):
        """
        returns float value
        """
        
        dot_index = str_value.find(".")
        comma_index = str_value.find(",")
        
        
        if dot_index>-1 and comma_index>-1: 
            
            if dot_index < comma_index:
                # "1.000,5" >> "1000.5"
                str_value = str_value.replace(".", "")
                str_value = str_value.replace(",", ".")
            else:
                # "1,000.5" >> "1000.5"
                str_value = str_value.replace(",", "")

        elif comma_index>-1:
            # "1,5" >> "1.5"
            str_value = str_value.replace(",", ".")
            
        return float(str_value)
    