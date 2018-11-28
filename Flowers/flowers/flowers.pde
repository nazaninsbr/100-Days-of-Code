int angle = 0; 

void setup(){
  size(640, 360); 
  background(102); 
  noStroke(); 
  fill(0, 102);
}

void draw(){
  if(mousePressed == true){
    angle += 10; 
    float val = cos(radians(angle))*12.0;
    for(int a = 0; a<360; a+= 75){
      float xoff = cos(radians(a))*val; 
      float yoff = sin(radians(a))*val; 
      fill(0); 
      ellipse(mouseX + xoff, mouseY + yoff, val, val);
    }
    fill(255); 
    ellipse(mouseX, mouseY, 2, 2);
  }
}