import java.util.ArrayList;
import java.util.Scanner;

public class Album{
  private ArrayList<musica>musica;
  private String genero; 
  private int ano;
  private String album;
  private String artista;

  public album(String genero, int ano, String album, String artista,String musica){
    this.genero = genero;
    this.ano = ano;
    this.album = album;
    this.artista = artista;
    this.musica = new ArrayList<musica>();
  }
  public addmusica(musica musica){
    
  }
}
