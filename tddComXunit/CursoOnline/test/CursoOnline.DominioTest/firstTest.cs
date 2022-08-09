using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace CursoOnline.DominioTest{
    public class firstTest{
        [Fact(DisplayName = "Test")]
        public void Test(){
            var var1 = 1;
            var var2 = 2;

            Assert.Equal(var1, var2);
        }
    }
}