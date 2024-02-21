class Product implements Comparable<Product> {
    private int id;
    private String name;
    private int dropChance;

    public Product(int id, String name, int dropChance){
        this.id = id;
        this.name = name;
        this.dropChance = dropChance;
    }

    public int getID(){
        return id;
    }
    public String getName(){
        return name;
    }
    public int getDropChance(){
        return dropChance;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }

        Product product = (Product) obj;
        if (product.getID() != id)
            return false;
        if (!product.getName().equals(name))
            return false;
        if (product.getDropChance() != dropChance)
            return false;
        return true;
    }

    @Override
    public int compareTo(Product o) {
        int temp = id - o.getID();

        if (temp == 0){
            temp = name.compareTo(o.getName());
            if (temp == 0)
                return dropChance - o.getDropChance();
        }

        return temp;
    }

    @Override
    public String toString() {
        return String.format("%d %s %d", id, name, dropChance);
    }
}