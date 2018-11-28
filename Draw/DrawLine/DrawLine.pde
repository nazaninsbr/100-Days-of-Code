void setup(){
  size(640, 360); 
  background(100); 
}

void draw(){
  stroke(255);
  if (mousePressed == true) {
    line(mouseX, mouseY, pmouseX, pmouseY); 
  }
}