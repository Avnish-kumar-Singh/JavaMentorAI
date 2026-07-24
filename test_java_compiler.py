"""
Test Java Compiler Tool
"""

from app.tools.java_compiler_tool import JavaCompilerTool


tool = JavaCompilerTool()


code = """
public class Main {
    public static void main(String[] args) {
        int x = 10 / 0;
        System.out.println(x);
    }
}
"""


result = tool.execute(code)

print(result)