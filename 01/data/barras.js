var url = 'https://raw.githubusercontent.com/aaizemberg/vis/gh-pages/01/data/poblacion.json';

d3.json( url ).then(function(data) {
  viz( data )
});

function viz(data) {

var svg = d3.select('body').append('svg').attr('width',800).attr('height',500);

svg.selectAll('text.provincias')
   .data(data).enter().append('text')
   .attr("class","provincias")
   .attr("text-anchor","end")
   .attr('x', 140-5)
   .attr('y', (d,i) => (i+1)*13 )
   .attr('fill','black')
   .text( d => d.provincia );

var max = d3.max(data.map(function(d) { return d.poblacion; }));

var escala = d3.scaleLinear().domain([0,max]).range([0,550]);

svg.selectAll('text.valores')
   .data(data).enter().append('text')
   .attr("class","valores")
   .attr('x', d => 5 + 140 + escala(d.poblacion) )
   .attr('y', (d,i) => (i+1)*13 )
   .attr('fill','black')
   .attr('font-size',12)
   .text( d => d.poblacion.toLocaleString('es-AR') );


svg.selectAll('rect')
   .data(data).enter().append('rect')
   .attr('x',140)
   .attr('y', (d,i) => i*13+1 )
   .attr('height', 12)
   .attr('fill','white')
     .append('title')
     .text( d => 'La provincia de ' + d.provincia + ' tiene ' + d.poblacion.toLocaleString('es-AR') + ' habitantes' )

d3.selectAll('rect').transition().duration(1000)
  .attr('width', d => escala(d.poblacion) )
  .attr('fill','grey');  
}
