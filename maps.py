import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def plate_draw(marker_color='red'):
    
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()  
    
    #
    ax.add_feature(cartopy.feature.LAND, facecolor='lightgreen')  
    ax.add_feature(cartopy.feature.OCEAN, facecolor='lightblue')  


    cities = {
        'Москва': (37.6173, 55.7558),
        'Нью-Йорк': (-74.0060, 40.7128),
        'Токио': (139.6917, 35.6895)
    }
    
    for city, (lon, lat) in cities.items():
        ax.plot(lon, lat, marker='o', color=marker_color, markersize=10)  
        ax.text(lon + 1, lat, city, fontsize=12, ha='left')  

    plt.savefig("out.png")
    plt.close()  

def mall_draw(marker_color='blue'):

    ax = plt.axes(projection=ccrs.Mollweide())
    ax.stock_img()  
    
    
    ax.add_feature(cartopy.feature.LAND, facecolor='lightgreen')  
    ax.add_feature(cartopy.feature.OCEAN, facecolor='lightblue')  

    
    cities = {
        'Москва': (37.6173, 55.7558),
        'Нью-Йорк': (-74.0060, 40.7128),
        'Токио': (139.6917, 35.6895)
    }
    
    for city, (lon, lat) in cities.items():
        ax.plot(lon, lat, marker='o', color=marker_color, markersize=10)  
        ax.text(lon + 1, lat, city, fontsize=12, ha='left')  

    plt.savefig("out1.png")
    plt.close() 

if __name__ == "__main__":
    plate_draw()  
    mall_draw()   
