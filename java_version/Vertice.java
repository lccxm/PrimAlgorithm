import java.util.Comparator;

public class Vertice implements Comparable<Vertice> {
    public static Comparator<Vertice> VerticeComparator;
    public int chave;
    public int val;
    public int w;
    public Vertice prev;
    private int INF = 9999;

    public Vertice(int val){
        this.val = val;
        this.chave = INF;
        this.prev = null;
    }

    @Override
    public String toString() {
        return "{" +
            " chave='" + chave + "'" +
            ", val='" + val + "'" +
            ", w='" + w + "'" +
                ", prev='" + prev + "'" +
            "}";
    }

    @Override
    public int compareTo(Vertice o) {
        return this.chave - o.chave;
    }


    public boolean equals(Object o) {
        if (this==o)
            return true;
        if(!(o instanceof Vertice))
            return false;
        Vertice v = (Vertice)o;
        return Integer.compare(this.val, v.val) == 0;
    }

}
