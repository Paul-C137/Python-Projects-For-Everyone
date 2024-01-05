import psutil

def get_total_storage():
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')
    
    # Retrieve the total storage in bytes
    total_storage_bytes = disk_usage.total
    
    # Convert bytes to gigabytes for better readability
    total_storage_gb = total_storage_bytes / (1024 ** 3)
    
    return total_storage_gb

def get_free_space():
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')
    
    # Retrieve the free space in bytes
    free_space_bytes = disk_usage.free
    
    # Convert bytes to gigabytes for better readability
    free_space_gb = free_space_bytes / (1024 ** 3)
    
    return free_space_gb

# Get the total storage and store it in the variable total_storage
total_storage = get_total_storage()
free_space = get_free_space()

print(f'Total Storage Available: {total_storage:.2f} GB')
print(f'Total Free Space: {free_space:.2f} GB')
